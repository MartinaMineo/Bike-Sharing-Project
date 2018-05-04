import pprint
import requests
import time
import json
import urllib2
import urllib
	

def HTTP_POST(lat, lng):
	#cnt = 1
	#while True:
		#lat = 22.5376
		#lng = 114.0577
		#payload = {'latitude': 22.5376, 'longitude': 114.0577}
	#try:
	
	# payload = {'latitude': lat, 'longitude': lng}
	# r = requests.post("https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do", data=payload)
	# r = r.text #+ '\n\n' + 'cnt: ' + str(cnt)
	
	url = "https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do" 
	headers = {"Referer": "https://servicewechat.com/","user-agent":"MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN"}
	payload = {'latitude': lat, 'longitude': lng}
	data = urllib.urlencode(payload)
	req = urllib2.Request(url, headers=headers, data=data)
	response=urllib2.urlopen(req)
	r = response.read()
	
	# except requests.exceptions.RequestException as err:
		# print ("OOps: Something Else",err)
	# except requests.exceptions.HTTPError as errh:
		# print ("Http Error:",errh)
	# except requests.exceptions.ConnectionError as errc:
		# print ("Error Connecting:",errc)
	# except requests.exceptions.Timeout as errt:
		# print ("Timeout Error:",errt)  

		#print(r)
		#print('\n')
		#print cnt
		#print ('*******************************************************************************')
		#with open('output.txt', 'a') as f:
		#	f.write(r)
		#time.sleep(10)
		#cnt +=1
	return r

		
		
def print_on_file(HTTP_response, file_name):
	 
	with open(file_name, 'a') as f:
		f.write(str(HTTP_response)+"\n")
		#f.write("******************************************************************************")
	
	return
	

