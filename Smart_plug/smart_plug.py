import url
import status

class smart_plug():
	def __init__(self,ip):
		self.ip=ip
		print 'Working'


	def SetID(self,id):
		self.ID=id

	def Category(self):
		print 'Category'
	
	def ON(self):
		url.on(self.ID)
	
	def OFF(self):
		url.off(self.ID) 

	def changeIP(self,ip):
		url.changeIP(ip)

	def changePORT(self,port):
		url.changePORT(port)

