#!/usr/bin/python
# -*- coding: utf-8 -*-

#facciamo acquiring and processing in parallelo
from book_class import Bookings
from park_class import Parkings
from ofo_funct import HTTP_POST
from multiprocessing import Process, Pool
import multiprocessing as mp
import time
import json
import copy

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
processes = []

lat1.append(45.516338)  #coordinate iniziali della citta di mialno
lng1.append(9.104160)
lat2.append(45.516338 - 0.0046) #punti iniziale dei cerchi sovrapposti
lng2.append(9.104160 + 0.0065)


start_time = int(time.time())

for i in range (1,10):  #numero di step da lat iniziale a lat finale della citta di milano
	lat1.append(lat1[-1] - 0.0092) #0.0046) #coefficiente per la conversione per 1 km in lat
for j in range (1,12):  #numero di step da long iniziale a long finale della citta di milano
	lng1.append(lng1[-1] + 0.013) #0.0065) #coefficiente per la conversione per 1 km in long
for ii in range (1,9):
	lat2.append(lat2[-1] - 0.0092)
for jj in range (1,11):
	lng2.append(lng2[-1] + 0.013)
	
lat.append(lat1+lat2)
lng.append(lng1+lng2)

output = mp.Queue()
counter = 0

lat  = lat[0]
lng = lng[0]

# print (lat1)
# print (lng1)

while True:

	for i in range(len(lat1)):
		inside_process=[]
		for j in range(len(lng1)):

		
	#while True:
			#print lat[i], lng[j]
			
			#for k in range (5):#pool = Pool(processes=5)
			#processes = [mp.Process(target=HTTP_POST, args=(lat[i], lng[j], output)) for x in range(4)]
			r = Process(target=HTTP_POST, args=(lat1[i], lng1[j], output))
			inside_process.append(r)
		processes.append(inside_process)

			#response = pool.map(HTTP_POST, lat[i], lng[j])
			
	#processes = [mp.Process(target=HTTP_POST, args=(lat[i], lng[j], output)) for x in range(220)]

	for i in range(len(lat2)):
		inside_process=[]
		for j in range(len(lng2)):
		
			r = Process(target=HTTP_POST, args=(lat2[i], lng2[j], output))
			inside_process.append(r)
		processes.append(inside_process)
		

	chitajoin_counter = 0
	start_counter = 0
	join_counter  = 0
	a = time.time()		
	for my_index in range(0,len(lat)):
		ip = processes[my_index]
		for p in ip:
			#print ("siamo in start")
			p.start()
			start_counter +=1
		print '=== start COUNTER === ' + str(start_counter)



		for p in ip:
			#print ("siamo in join")
			join_counter += 1
			p.join(0.05)


	print '*** JOIN COUNTER *** ' + str(join_counter)
	print '*** QS ***' + str(output.qsize())

	results = ''
	ip_count = 0

	for i in range(output.qsize()):
		results += output.get()
	'''
	for ip in processes:
		print(ip_count)
		p_count = 0
		for p in ip:
			print (ip_count, p_count)
			if ip_count == 9 and p_count ==11:
				print output.get()

			results +=output.get() +','
			p_count+=1
		ip_count +=1
		print 

	'''
	print time.time() - a 

	print (time.strftime("%H:%M:%S"))


#exit()


# for res in results:
	# data = json.loads(res)
	

		# #r = HTTP_POST(lat[i], lng[j])
		# #response = HTTP_POST(lat[i], lng[j])#45.463657, 9.190177) #coordinate di Milano
		# #r = "[" + response + "]"
		
		# #filename = "merd.txt"   #"28_05_2018_22_06_30.txt"  
		# #with open(filename) as f:
			# #data = json.load(f)   #in data abbiamo tutto il file
			
		# # data = json.loads(r)

	# for i in range (len(data)):          #per ogni blocco prendo il numero di elementi prima avevamo messo 3 per provare i primi tre blocchi del file merd
		# data_tmp = data[i]["values"]["cars"]
		# data_tmp_IDs = []
		# print "***********************************************************"
		
		# for j in range (len(data_tmp)):
			# bikeID = data_tmp[j]["carno"]
			# data_tmp_IDs.append(data_tmp[j]["carno"])
			# if bikeID not in activeParkings.keys():		#se la bici al tempo 1 non e presente negli active parking e al tempo 2 e spuntata vuol dire che e stata posteggiata 			
				# #activeParkings[bikeID] = Parkings(data_tmp[j]["datetime"], None, data_tmp[j]["lng"], data_tmp[j]["lat"], bikeID)	#sta iniziando un nuovo parking
				# activeParkings[bikeID] = Parkings(int(time.time()), None, data_tmp[j]["lng"], data_tmp[j]["lat"], bikeID)	#nel caso real time 
				# print "sto aggiungendo il parking:   " + bikeID
				# if bikeID in activeBookings.keys():
					# activeBookings[bikeID].set_final_time(int(time.time()))  #settiamo il tempo la lng e la lat del fine noleggio che coincidono con quelli di inizio parcheggio
					# activeBookings[bikeID].set_final_lng(data_tmp[j]["lng"])
					# activeBookings[bikeID].set_final_lat(data_tmp[j]["lat"])
					# permanentBookings[bikeID] = copy.deepcopy(activeBookings[bikeID])#inserire bici in permanent bookings
					# activeBookings.pop(bikeID, None)#togliere bici da activeBookings
					# print "sto rimuovendo un booking:   " + bikeID
				
		# for element in activeParkings.keys():  #per gli elementi in activeParkings se l elemento non e nel blocco della risposta all API allora il parcheggio e diventato storico
			# if element not in data_tmp_IDs: #data_tmp_IDs sono i vari blocchi -> risposte all API
				# activeParkings[element].set_final_time(int(time.time()))
				# activeBookings[element] = Bookings(activeParkings[element].get_final_time(), None, activeParkings[element].get_lng(), activeParkings[element].get_lat(), None, None, element) #inizia un bookings
				# print "sto aggiungendo un booking:   " + element
				# permanentParkings[element] = copy.deepcopy(activeParkings[element])
				# activeParkings.pop(element, None)
				# print "sto rimuovendo un parking:   "+ element

		# print "Active Parkings: ",  len(activeParkings)		
		# print "Active Bookings: ",  len(activeBookings)
		# print "Permanent Parkings: ",  len(permanentParkings)
		# print "Permanent Bookings: ",  len(permanentBookings)
		
		# time.sleep(60) #un minuto di time sleep
		
			
# result = []	
# for proc in jobs:
	# proc.join()
	# print ("siamo qui")
	# print (str(proc.exitcode))
	# result.append(proc.exitcode)
	# data = json.loads(proc.exitcode)
	
	# for i in range (len(data)):          #per ogni blocco prendo il numero di elementi prima avevamo messo 3 per provare i primi tre blocchi del file merd
			# data_tmp = data[i]["values"]["cars"]
			# data_tmp_IDs = []
			# print "***********************************************************"
			
			# for j in range (len(data_tmp)):
				# bikeID = data_tmp[j]["carno"]
				# data_tmp_IDs.append(data_tmp[j]["carno"])
				# if bikeID not in activeParkings.keys():		#se la bici al tempo 1 non e presente negli active parking e al tempo 2 e spuntata vuol dire che e stata posteggiata 			
					# #activeParkings[bikeID] = Parkings(data_tmp[j]["datetime"], None, data_tmp[j]["lng"], data_tmp[j]["lat"], bikeID)	#sta iniziando un nuovo parking
					# activeParkings[bikeID] = Parkings(int(time.time()), None, data_tmp[j]["lng"], data_tmp[j]["lat"], bikeID)	#nel caso real time 
					# print "sto aggiungendo il parking:   " + bikeID
					# if bikeID in activeBookings.keys():
						# activeBookings[bikeID].set_final_time(int(time.time()))  #settiamo il tempo la lng e la lat del fine noleggio che coincidono con quelli di inizio parcheggio
						# activeBookings[bikeID].set_final_lng(data_tmp[j]["lng"])
						# activeBookings[bikeID].set_final_lat(data_tmp[j]["lat"])
						# permanentBookings[bikeID] = copy.deepcopy(activeBookings[bikeID])#inserire bici in permanent bookings
						# activeBookings.pop(bikeID, None)#togliere bici da activeBookings
						# print "sto rimuovendo un booking:   " + bikeID
					
			# for element in activeParkings.keys():  #per gli elementi in activeParkings se l elemento non e nel blocco della risposta all API allora il parcheggio e diventato storico
				# if element not in data_tmp_IDs: #data_tmp_IDs sono i vari blocchi -> risposte all API
					# activeParkings[element].set_final_time(int(time.time()))
					# activeBookings[element] = Bookings(activeParkings[element].get_final_time(), None, activeParkings[element].get_lng(), activeParkings[element].get_lat(), None, None, element) #inizia un bookings
					# print "sto aggiungendo un booking:   " + element
					# permanentParkings[element] = copy.deepcopy(activeParkings[element])
					# activeParkings.pop(element, None)
					# print "sto rimuovendo un parking:   "+ element

			# print "Active Parkings: ",  len(activeParkings)		
			# print "Active Bookings: ",  len(activeBookings)
			# print "Permanent Parkings: ",  len(permanentParkings)
			# print "Permanent Bookings: ",  len(permanentBookings)

			
			#time.sleep(60) #un minuto di time sleep
		 
# duration = (int(time.time()) - start_time)/60    #ho la durata in minuti  #abbiamo visto che impiega 22 minuti per girare
# print duration
