from url import *
import status

url=url()

class smart_plug():
	def __init__(self,ip,port):
		self.ip=ip
		self.port=port
		self.status=0
		url.setIP(self.ip)
		url.setPORT(self.port)

	def SetID(self,id):
		self.ID=id

	def GetID(self):
		return self.ID

	def Category(self):
		return 'Category'

	def GetStatus(self):
		return self.status

	def changeStatus(self):
		if (self.status == 1):
			self.OFF()
		else:
			self.ON()
	
	def ON(self):
		url.on(self.ID)
		self.status = 1
		
	def OFF(self):
		url.off(self.ID)
		self.status = 0

	def changeIP(self,ip):
		url.changeIP(ip)

	def changePORT(self,port):
		url.changePORT(port)

