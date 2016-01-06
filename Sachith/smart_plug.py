import my_url
import status

class SmartPlug(object):

	def __init__(self):
		self.status=status

	def ID(self):
		return 4

	def Category(self):
		return 1
	
	def ON(self):
		my_url.on()
	
	def OFF(self):
		my_url.off()

test=SmartPlug()

test.ON()
