#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import strftime
from ofo_funct import HTTP_POST
from ofo_funct import print_on_file, print_on_file2
from ofo_funct import print_opened_bracket_on_file, print_closed_bracket_on_file
import time
import json


num_cicli = 60 * 3 #un' ora di dati se ne vogliamo di piu' possiamo moltiplicare per quante ore vogliamo
num_cicli_file = 30
cnt = 1

name_file_tmp = strftime("%d_%m_%Y %H_%M_%S")
name_file = str(name_file_tmp) + '.txt'
print_opened_bracket_on_file(name_file)

for i in range(num_cicli):
	
	response = HTTP_POST(45.463657, 9.190177)

	if i % num_cicli_file == 0 and i != 0: #in questo modo aggiorniamo il nome del file ogni 30 min (1800 secondi)	 se faccio una sleep di 10 secondi devo fare modulo 180 mentre per un minuto modulo 1800/60
		print_closed_bracket_on_file(name_file)
		name_file_tmp = strftime("%d_%m_%Y %H_%M_%S")
		name_file = str(name_file_tmp) + '.txt'
		print_opened_bracket_on_file(name_file)
		print_on_file(response, name_file)
		cnt += 1
	
	elif i == ((num_cicli - (num_cicli/num_cicli_file - 1*cnt) * num_cicli_file) - 1):
		name_file = name_file
		print_on_file2(response, name_file)
		
	else:
		name_file = name_file
		print_on_file(response, name_file)
	
	#print_on_file(response, name_file)
	
	time.sleep(60)

print_closed_bracket_on_file(name_file)
