##SCRIPT CENTRALE##

#!/usr/bin/python
# -*- coding: utf-8 -*-

#facciamo acquiring and processing in parallelo
from book_class import Bookings
from park_class import Parkings
import time
import json
import copy
import os

#init_time, final_time, lng, lat, bikeID
#init_time, final_time, init_lng, init_lat, final_lng, final_lat, bikeID

activeParkings = {}
permanentParkings = {}

activeBookings = {}
permanentBookings = {}

lat = []
lng = []
lat1 = []
lng1 = []
lat2 = []
lng2 = []

lat1.append(45.516338)  #coordinate iniziali della citta di milano
lng1.append(9.104160)
lat2.append(45.516338 - 0.0046) #punti iniziale dei cerchi sovrapposti
lng2.append(9.104160 + 0.0065)

#start_time = int(time.time())

for i in range (1,10):  #numero di step da lat iniziale a lat finale della citta di milano
	lat1.append(lat1[-1] - 0.0092) #0.0046) #coefficiente per la conversione per 1 km in lat
for j in range (1,12):  #numero di step da long iniziale a long finale della citta di milano
	lng1.append(lng1[-1] + 0.013) #0.0065) #coefficiente per la conversione per 1 km in long
for ii in range (1,9):
	lat2.append(lat2[-1] - 0.0092)
for jj in range (1,11):
	lng2.append(lng2[-1] + 0.013)
	

for iter in range (12):

	for i in range (len(lat1)):
		for j in range (len(lng1)):
			cmd = "wget https://one.ofo.com/nearbyofoCar --post-data=\"content-type=application/x-www-form-urlencoded&lat="+str(lat1[i])+"&lng="+str(lng1[j])+"&source=1&token=87c37060-8033-11e8-8a4e-0f6efcf06228\" -O - >> response.txt"
			cmd2 = "echo "" >> response.txt"  
			os.system(cmd)
			os.system(cmd2)			
			
	for i in range (len(lat2)):
		for j in range (len(lng2)):
			cmd = "wget https://one.ofo.com/nearbyofoCar --post-data=\"content-type=application/x-www-form-urlencoded&lat="+str(lat2[i])+"&lng="+str(lng2[j])+"&source=1&token=87c37060-8033-11e8-8a4e-0f6efcf06228\" -O - >> response.txt"
			cmd2 = "echo "" >> response.txt"
			os.system(cmd)
			os.system(cmd2)	
	

	data_tmp_IDs = []
			
	filename = "response.txt" 
	with open(filename) as f:
		blocks = f.readlines()  #divide il file in blocchi

	for b in blocks:    #b rappresenta un blocco
		if len(b) < 3:
			pass
		else:
			jsonblock = json.loads(b)   #in data abbiamo un blocco solo in json
			
			try:
				data_tmp = jsonblock["values"]["cars"] #lista di bici in un blocco
			
			except:
				print "siamo in except "
			
			print "***********************************************************"
			
			for j in range (len(data_tmp)):
				bikeID = data_tmp[j]["carno"]
				if bikeID not in data_tmp_IDs:   #in questo modo eliminiamo i doppioni
					data_tmp_IDs.append(bikeID)
					#data_tmp_IDs.append(data_tmp[j]["carno"])
					
					if bikeID not in activeParkings.keys():		#se la bici al tempo 1 non e presente negli active parking e al tempo 2 e spuntata vuol dire che e stata posteggiata 			
						#activeParkings[bikeID] = Parkings(data_tmp[j]["datetime"], None, data_tmp[j]["lng"], data_tmp[j]["lat"], bikeID)	#sta iniziando un nuovo parking
						activeParkings[bikeID] = Parkings(int(time.time()), None, data_tmp[j]["lng"], data_tmp[j]["lat"], bikeID)	#nel caso real time 
						print "sto aggiungendo il parking:   " + bikeID
						if bikeID in activeBookings.keys():
							activeBookings[bikeID].set_final_time(int(time.time()))  #settiamo il tempo la lng e la lat del fine noleggio che coincidono con quelli di inizio parcheggio
							activeBookings[bikeID].set_final_lng(data_tmp[j]["lng"])
							activeBookings[bikeID].set_final_lat(data_tmp[j]["lat"])
							permanentBookings[bikeID] = copy.deepcopy(activeBookings[bikeID])#inserire bici in permanent bookings
							activeBookings.pop(bikeID, None)#togliere bici da activeBookings
							print "sto rimuovendo un booking:   " + bikeID
				
	for element in activeParkings.keys():  #per gli elementi in activeParkings se l elemento non e nel blocco della risposta all API allora il parcheggio e diventato storico
		if element not in data_tmp_IDs: #data_tmp_IDs sono i vari blocchi -> risposte all API
			activeParkings[element].set_final_time(int(time.time()))
			activeBookings[element] = Bookings(activeParkings[element].get_final_time(), None, activeParkings[element].get_lng(), activeParkings[element].get_lat(), None, None, element) #inizia un bookings
			print "sto aggiungendo un booking:   " + element
			permanentParkings[element] = copy.deepcopy(activeParkings[element])
			activeParkings.pop(element, None)
			print "sto rimuovendo un parking:   "+ element

	print "Active Parkings: ",  len(activeParkings)		
	print "Active Bookings: ",  len(activeBookings)
	print "Permanent Parkings: ",  len(permanentParkings)
	print "Permanent Bookings: ",  len(permanentBookings)

	time.sleep(60) #un minuto di time sleep
	
	with open(filename, "w"):  #in questo modo cancelliamo il contenuto del file per evitare che vengano considerate sempre le stesse biciclette
		pass

	# duration = (int(time.time()) - start_time)/60    #ho la durata in minuti  #abbiamo visto che impiega 22 minuti per girare
	# print duration
	
	