from smart_plug_connection import *
import time

smart_plug_connection=smart_plug_connection()

class switch():
	def __init__(self,ip,port,id):
		self.ip=ip
		self.ID=id
		self.port=port
		self.status=0
		self.intensity=0
		self.category='Assign me in to a category'
		smart_plug_connection.setIP(self.ip)
		smart_plug_connection.setPORT(self.port)
		#self.setOff()

	def getId(self):
		return self.ID

	def getWhoIm(self):
		return self.category

	def setCategory(self,category):
		self.category=category

	def getStatus(self):
		return self.status

	def changeStatus(self):
		if (self.status==1):
			self.setOff()
		else:
			self.setOn()

	def setIntensity(self,intensity):
		if(intensity>128):
			smart_plug_connection.setOn(self.ID)
			self.status = 1
		else:
			smart_plug_connection.setOff(self.ID)
			self.status = 0

	def getIntensity(self):
		if(self.status==1):
			return '255'
		else:
			return '0'

	def setParameter(self,parameter):
		print "no parameter option"
		#self.parameter=parameter

	def getParameter(self):
		return self.parameter

	def setOn(self):
		smart_plug_connection.setOn(self.ID)
		self.status = 1
		
	def setOff(self):
		smart_plug_connection.setOff(self.ID)
		self.status = 0

	def Param_Increase(self,value=30):
		smart_plug_connection.setOn(self.ID)
		self.status = 1

	def Param_Decrease(self,value=30):
		smart_plug_connection.setOff(self.ID)
		self.status = 0

	def Increase(self):
		smart_plug_connection.setOn(self.ID)
		self.status = 1

	def Decrease(self):
		smart_plug_connection.setOff(self.ID)
		self.status = 0

	def copy(self):
        return -1
        
    def paste(self,data):
        return -1