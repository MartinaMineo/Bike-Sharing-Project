import json
import time

class Bookings():

	# activeBookings = []
	# activeBookings.append({"timestamp":"", "lng":"", "lat":"", "bomNum":"", "carno":"", "userIdLast":""}) #stessi campi di cars
	#activeBookings = {"timestamp":"", "lng":"", "lat":"", "bomNum":"", "carno":"", "userIdLast":""}
	
	# permanentBookings = []
	#permanentBookings.append({"init_time":"", "final_time":"", "init_lng":"", "final_lng":"", "init_lat":"", "final_lat":"", "carno":""})
	#permanentBookings = {"init_time":"", "final_time":"", "init_lng":"", "final_lng":"", "init_lat":"", "final_lat":"", "carno":""}
	
	def __init__ (self, init_time, final_time, init_lng, init_lat, final_lng, final_lat, bikeID):
		self.init_time = init_time
		self.final_time = final_time
		self.init_lng = init_lng
		self.init_lat = init_lat
		self.final_lng = final_lng
		self.final_lat = final_lat
		self.bikeID = bikeID
		
	
	def set_init_time(self, init_time):
		self.init_time = init_time
		return
	
	def set_final_time(self, final_time):
		self.final_time = final_time
		return

	def set_init_lng(self, init_lng):
		self.init_lng = init_lng
		return
		
	def set_init_lat(self, init_lat):
		self.init_lat = init_lat
		return
		
	def set_final_lng(self, final_lng):
		self.final_lng = final_lng
		return	
	
	def set_final_lat(self, final_lat):
		self.final_lat = final_lat
		return		
	
	def get_final_time(self):
		return self.final_time
		
	def get_init_lng(self):
		return self.init_lng
		
	def get_init_lat(self):
		return self.init_lat	
		
		
		# for key in bookings_dict:
			# if key == "init_time":
				# self.init_time = bookings_dict[key]
			# elif key == "final_time":
				# self.final_time = bookings_dict[key]
			# elif key == "init_lng":
				# self.init_lng = bookings_dict[key]
			# elif key == "final_lng":
				# self.final_lng = bookings_dict[key]
			# elif key == "init_lat":
				# self.init_lat = bookings_dict[key]
			# elif key == "final_lat":
				# self.final_lat = bookings_dict[key]
			# elif key == "carno":
				# self.carno = bookings_dict[key]
		
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		