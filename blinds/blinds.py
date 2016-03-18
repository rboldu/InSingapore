from blinds_connection import *
import time

blinds_connection=blinds_connection()

class blinds():
	def __init__(self,ip,port,id):
		self.ip=ip
		self.id=id
		self.device_id=8
		self.port=port
		self.status=0
		self.intensity=0
		self.category='I am a blind'
		blinds_connection.setIP(self.ip)
		blinds_connection.setPORT(self.port)
		#if(id==1):
		#	self.device_id=10
		#else:
		#	self.device_id=0
		#self.setOff()

	def getId(self):
		return self.id

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
			blinds_connection.setOn(self.device_id)
			self.status = 1
		else:
			blinds_connection.setOff(self.device_id)
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
		blinds_connection.setUp(self.device_id)
		self.status = 1
		
	def setOff(self):
		blinds_connection.setDown(self.device_id)
		self.status = 0

	def Param_Increase(self,value=30):
		blinds_connection.setUp(self.device_id)
		self.status = 1

	def Param_Decrease(self,value=30):
		blinds_connection.setDown(self.device_id)
		self.status = 0

	def Increase(self):
		blinds_connection.setUp(self.device_id)
		self.status = 1

	def Decrease(self):
		blinds_connection.setDown(self.device_id)
		self.status = 0

	def copy(self):
		return -1

	def paste(self,data):
		return -1