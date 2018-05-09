#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib2
import urllib
import time
import datetime


def HTTP_POST(lat, lng):
	url = "https://one.ofo.com/nearbyofoCar" 
	headers = {"content-type": "application/x-www-form-urlencoded"}
	payload = {'lat': lat, 'lng': lng, 'source': 1, 'token': "595d4f30-4f77-11e8-a4b0-5196d0a1885f"}
	data = urllib.urlencode(payload)
	req = urllib2.Request(url, headers=headers, data=data)
	response=urllib2.urlopen(req)
	r = response.read()
	#print (r)
	return r
	
	
def print_on_file(HTTP_response, file_name):
	 
	with open(file_name, 'a') as f:
		f.write(str(HTTP_response)+",\n")
		#f.write(str(HTTP_response)+'\n'+'\n'+ str(datetime.datetime.now())+'\n'+'\n')#time.strftime("%Y-%m-%d %H:%M:%S")+'\n'+'\n')
		#f.close()
	return
	
def print_on_file2(HTTP_response, file_name):
	 
	with open(file_name, 'a') as f:
		f.write(str(HTTP_response)+"\n")
		#f.write(str(HTTP_response)+'\n'+'\n'+ str(datetime.datetime.now())+'\n'+'\n')#time.strftime("%Y-%m-%d %H:%M:%S")+'\n'+'\n')
		#f.close()
	return
	
def print_opened_bracket_on_file(file_name):
	f = open(file_name, 'a')
	f.write('[')
	return
	
def print_closed_bracket_on_file(file_name):
	f = open(file_name, 'a')
	f.write(']')
	return