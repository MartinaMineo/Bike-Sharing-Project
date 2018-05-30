import json
import time

class Parkings():

	# activeParkings = []
	# activeParkings.append({"timestamp":"", "lng":"", "lat":"", "bomNum":"", "carno":"", "userIdLast":""}) #stessi campi di cars poi timestamp diventera datetime
	# activeParkings = {"timestamp":"", "lng":"", "lat":"", "bomNum":"", "carno":"", "userIdLast":""}
	
	# permanentParkings = []
	# permanentParkings.append({"init_time":"", "final_time":"", "lng":"", "lat":"", "carno":""})
	#permanentParkings = {"init_time":"", "final_time":"", "lng":"", "lat":"", "carno":""}
		
	def __init__ (self, init_time, final_time, lng, lat, bikeID):
		self.init_time = init_time
		self.final_time = final_time
		self.lng = lng
		self.lat = lat
		self.bikeID = bikeID
		
		
		# for key in parkings_dict:
			# if key == "init_time":
				# self.init_time = parkings_dict[key]
			# elif key == "final_time":
				# self.final_time = parkings_dict[key]
			# elif key == "lng":
				# self.lng = parkings_dict[key]
			# elif key == "lat":
				# self.lat = parkings_dict[key]
			# elif key == "carno":
				# self.carno = parkings_dict[key]
				
	def set_final_time(self, final_time):
		self.final_time = final_time
		return
		
	def get_final_time(self):
		return self.final_time
		
	def get_lng(self):
		return self.lng
		
	def get_lat(self):
		return self.lat	
		
		
		
		