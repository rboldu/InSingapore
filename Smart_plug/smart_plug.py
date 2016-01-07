from url import *
import status

url=url()

class smart_plug():
	def __init__(self,ip,port):
		self.ip=ip
		self.port=port
		url.setIP(self.ip)
		url.setPORT(self.port)
		print 'Working'+self.ip+self.port

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

