from ispy_connection import *

ispy_connection=ispy_connection()

class ispy_tank():
	def __init__(self,ip,port,id):
		self.ip=ip
		self.port=port
		self.ID=id
		ispy_connection.setIP(self.ip)
		ispy_connection.setPORT(self.port)

	def getId(self):
		return self.ID

	def getWhoIm(self):
		return "iSpy tank"

	def changeStatus(self):
		return -1

	def setIntensity(self,intensity):
		return -1

	def setOn(self):
		ispy_connection.forward()

	def setOff(self):
		ispy_connection.stop()
	
	def setParameter(self,parameter):
		return -1
	
	def getParameter(self):
		return -1
	
	def getStatus(self):
		return -1
	
	def Increase(self,value):
		ispy_connection.forward()
	
	def Decrease(self,value):
		ispy_connection.backward()

	def Param_Increase(self,value):
		ispy_connection.turn_right()

	def Param_Decrease(self,value):
		ispy_connection.turn_left()

	def copy(self):
		return -1
	
	def paste(self,data):
		return -1
