from Smart_plug_connection import *

Smart_plug_connection=Smart_plug_connection()

class smart_plug():
	def __init__(self,ip,port):
		self.ip=ip
		self.port=port
		self.status=0
		Smart_plug_connection.setIP(self.ip)
		Smart_plug_connection.setPORT(self.port)

	def setId(self,id):
		self.ID=id

	def getId(self):
		return self.ID

	def getWhoIm(self):
		return 'Type'

	def getStatus(self):
		return self.status

	def changeStatus(self):
		if (self.status == 1):
			self.setOff()
		else:
			self.setOn()

	def setIntensity(self,intensity):
		self.intensity=intensity

	def setParameter(self,parameter):
		self.parameter=parameter

	def getParameter(self):
		return self.parameter

	def setOn(self):
		Smart_plug_connection.setOn(self.ID)
		self.status = 1
		
	def setOff(self):
		Smart_plug_connection.setOff(self.ID)
		self.status = 0

	def changeIP(self,ip):
		Smart_plug_connection.changeIP(ip)

	def changePORT(self,port):
		Smart_plug_connection.changePORT(port)

