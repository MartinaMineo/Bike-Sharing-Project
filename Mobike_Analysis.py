from time import strftime
from Mobike_funct import HTTP_POST
from Mobike_funct import print_on_file
import time
import json


num_cicli = 360 #un' ora di dati se ne vogliamo di piu' possiamo moltiplicare per quante ore vogliamo

name_file_tmp = strftime("%d_%m_%Y %H_%M")
name_file = str(name_file_tmp) + '.txt'


for i in range(num_cicli):
	#data1 = "config_file.json"
	#data = open('config_file.json') as json_data_file
	#data3 = data2.read()
	#data1 = json.loads(json_data_file)
	
	response = HTTP_POST(45.075861, 7.671576)  #22.5376, 114.0577) #lat e lng usate sono di TORINO (pressi piazza statuto) # HTTP_POST(data["TORINO"][0], data["TORINO"][1])

	if i % 180 == 0: #in questo modo aggiorniamo il nome del file ogni 30 min (1800 secondi)	 se faccio una sleep di 10 secondi devo fare modulo 180 mentre per un minuto modulo 1800/60						
		name_file_tmp = strftime("%d_%m_%Y %H_%M")
		name_file = str(name_file_tmp) + '.txt'
	else:
		name_file = name_file
	
	print_on_file(response, name_file)
	
	time.sleep(10)
