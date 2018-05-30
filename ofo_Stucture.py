#!/usr/bin/python
# -*- coding: utf-8 -*-

#facciamo acquiring and processing in parallelo
from book_class import Bookings
from park_class import Parkings
from ofo_funct import HTTP_POST
import time
import json
import copy


filename = "merd.txt" #"28_05_2018_22_06_30.txt"
with open(filename) as f:
	data = json.load(f)   #in data abbiamo tutto il file


activeParkings = {}
permanentParkings = {}

activeBookings = {}
permanentBookings = {}

#init_time, final_time, lng, lat, bikeID
#init_time, final_time, init_lng, init_lat, final_lng, final_lat, bikeID

for i in range  (3): #(len(data)):          #per ogni blocco prendo il numero di elementi 
	data_tmp = data[i]["values"]["cars"]
	data_tmp_IDs = []
	print "***********************************************************"
	
	for j in range (len(data_tmp)):
		bikeID = data_tmp[j]["carno"]
		data_tmp_IDs.append(data_tmp[j]["carno"])
		if bikeID not in activeParkings.keys():		#se la bici al tempo 1 non e presente negli active parking e al tempo 2 e spuntata vuol dire che e stata posteggiata 			
			activeParkings[bikeID] = Parkings(data_tmp[j]["datetime"], None, data_tmp[j]["lng"], data_tmp[j]["lat"], bikeID)	#sta iniziando un nuovo parking
			#activeParkings[bikeID] = Parkings(int(time.time()), None, data_tmp[j]["lng"], data_tmp[j]["lat"], bikeID)	#nel caso real time 
			print "sto aggiungendo il parking:   " + bikeID
			if bikeID in activeBookings.keys():
				activeBookings[bikeID].set_final_time(int(time.time()))  #settiamo il tempo la lng e la lat del fine noleggio che coincidono con quelli di inizio parcheggio
				activeBookings[bikeID].set_final_lng(data_tmp[j]["lng"])
				activeBookings[bikeID].set_final_lat(data_tmp[j]["lat"])
				permanentBookings[bikeID] = copy.deepcopy(activeBookings[bikeID])#inserire bici in permanent bookings
				activeBookings.pop(bikeID, None)#togliere bici da activeBookings
				print "sto rimuovendo un booking:   " + bikeID
			
	for element in activeParkings.keys():  #per gli elementi in activeParkings se l elemento non e nel blocco della risposta all API allora il parcheggio e diventato storico
		if element not in data_tmp_IDs:
			activeParkings[element].set_final_time(int(time.time()))
			activeBookings[element] = Bookings(activeParkings[element].get_final_time(), None, activeParkings[element].get_lng(), activeParkings[element].get_lat(), None, None, element) #inizia un bookings
			print "sto aggiungendo un booking:   " + element
			permanentParkings[element] = copy.deepcopy(activeParkings[element])
			activeParkings.pop(element, None)
			print "sto rimuovendo un parking:   "+ element
	
#print len(activeParkings)		
		
		
		#deve ritornare il timestamp in caso di real time piu currentParkingsFromApi
		
		#response = HTTP_POST(45.463657, 9.190177) #coordinate di Milano
		
		#time.sleep(60) #un minuto di time sleep
