#!/usr/bin/python
import requests
import time
import urllib2
import urllib

#################### GOBEEBIKE - Hong Kong ####################
# cnt = 0
# while True:

	# response = requests.get('https://appaws.gobee.bike/GobeeBike/bikes/near_bikes?accuracy=20&lat=22.38&lng=114.198')
	# print(response.text)
	# print ('*******************************************************************************')
	# time.sleep( 900 ) #serve per stampare i dati dopo un tot di secondi per evitare di avere sempre gli stessi 900sec = 1/4 d'ora
	# cnt +=1
	
#################### BYKE - Berlin ####################
# cnt = 0
# while True:
	# response = requests.get('https://api-prod.ibyke.io/v1/bikes?latitude=52.55001&longitude=13.40902&order=nearby')
	# print(response.text)
	# print ('*******************************************************************************')
	# time.sleep( 900 ) #serve per stampare i dati dopo un tot di secondi per evitare di avere sempre gli stessi 900sec = 1/4 d'ora
	# cnt +=1
	
#################### OnzO - New Zealand ####################
# cnt = 0
# while True:
	# response = requests.get('https://app.onzo.co.nz/nearby/-36.848123/174.765588/50.0')
	# print(response.text)
	# print ('*******************************************************************************')
	# time.sleep( 900 ) #serve per stampare i dati dopo un tot di secondi per evitare di avere sempre gli stessi 900sec = 1/4 d'ora
	# cnt +=1
	
#################### Dropbike - Toronto ####################
# cnt = 0
# while True:
	# url = "https://dropbikeadminapi.herokuapp.com/v1/bikes_nearby"
	# values = '{"lat": 43.659415191015498, "lng": -79.395512826740742}'
	# headers = {"Content-Type":"application/json"}
	# req = urllib2.Request(url, data=values, headers=headers)
	# response=urllib2.urlopen(req)
	# response.close()
	# print (response.read())
	# print ('*******************************************************************************')
	# time.sleep( 900 ) #serve per stampare i dati dopo un tot di secondi per evitare di avere sempre gli stessi 900sec = 1/4 d'ora
	# cnt +=1

#################### Mobike  - China  ####################
 
# cnt = 0
# while True:
	# payload = {'latitude': 22.5376, 'longitude': 114.0577}
	# r = requests.post("https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do", data=payload)
	# print(r.text)
	# print ('*******************************************************************************')
	# time.sleep(10)
	# cnt +=1
	
	
	
	###PROVA mobike con urllib2###
cnt = 0
while True:
	url = "https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do" 
	headers = {"Referer": "https://servicewechat.com/","user-agent":"MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN"}
	payload = {'latitude': 22.5376, 'longitude': 114.0577}
	data = urllib.urlencode(payload)
	req = urllib2.Request(url, headers=headers, data=data)
	response=urllib2.urlopen(req)
	# # response.close()
	print (response.read())
	print ('*******************************************************************************')
	time.sleep(1) #serve per stampare i dati dopo un tot di secondi per evitare di avere sempre gli stessi 900sec = 1/4 d'ora
	cnt +=1

#################### JUMP - Washington, DC ####################
# cnt = 0
# while True:

	# response = requests.get('https://dc.jumpmobility.com/opendata/free_bike_status.json')
	# print(response.text)
	# print ('*******************************************************************************')
	# time.sleep( 900 ) #serve per stampare i dati dopo un tot di secondi per evitare di avere sempre gli stessi 900sec = 1/4 d'ora
	# cnt +=1
	
#################### Call a bike  -   ####################
# cnt = 0
# while True:
	# url = "https://api.deutschebahn.com/flinkster-api-ng/v1/bookingproposals?lat=48.15&lon=11.5&radius=5000&limit=100&providernetwork=2" 
	# # al posto di bookingproposals si possono mettere altri campi come /areas, /providernetworks/{providernetworkUID}/rentalobjects/{rentalObjectUID}, ecc.. 
	# # guarda sito -> https://developer.deutschebahn.com/store/apis/info?name=Flinkster_API_NG&version=v1&provider=DBOpenData#!/bookingproposals/listBookingProposals
	# headers = {"Accept": "application/json","Authorization":"Bearer 8b1986a74775cfb5aebbe678bf5bcd77"}
	# req = urllib2.Request(url, headers=headers)
	# response=urllib2.urlopen(req)
	# # response.close()
	# print (response.read())
	# print ('*******************************************************************************')
	# time.sleep( 900 ) #serve per stampare i dati dopo un tot di secondi per evitare di avere sempre gli stessi 900sec = 1/4 d'ora
	# cnt +=1
