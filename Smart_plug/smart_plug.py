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

	def setId(self,id):
		self.ID=id

	def getId(self):
		return self.ID

	def category(self):
		return 'Category'

	def getStatus(self):
		return self.status

	def changeStatus(self):
		if (self.status == 1):
			self.setOff()
		else:
			self.setOn()
	
	def setOn(self):
		url.setOn(self.ID)
		self.status = 1
		
	def setOff(self):
		url.setOff(self.ID)
		self.status = 0

	def changeIP(self,ip):
		url.changeIP(ip)

	def changePORT(self,port):
		url.changePORT(port)

