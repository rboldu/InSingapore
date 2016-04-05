from ispy_connection_rp import *
import time
delay=0.5

ispy_connection=ispy_connection_rp()

class ispy_tank():
	def __init__(self,ip_rp,id):
		self.id=id
		self.ip_rp=ip_rp

	def getId(self):
		return self.id

	def getWhoIm(self):
		return "iSpy tank"

	def changeStatus(self):
		return -1

	def setIntensity(self,intensity):
		return -1

	def setOn(self):
		ispy_connection.forward(self.ip_rp)
		time.sleep(delay)
		ispy_connection.stop(self.ip_rp)

	def setOff(self):
		ispy_connection.stop(self.ip_rp)
	
	def setParameter(self,parameter):
		return -1
	
	def getParameter(self):
		return -1
	
	def getStatus(self):
		return -1
	
	def Increase(self,value=30):
		ispy_connection.forward(self.ip_rp)
		time.sleep(delay)
		ispy_connection.stop(self.ip_rp)
	
	def Decrease(self,value=30):
		ispy_connection.backward(self.ip_rp)
		time.sleep(delay)
		ispy_connection.stop(self.ip_rp)
	
	def Param_Increase(self,value=30):
		ispy_connection.turn_right(self.ip_rp)
		time.sleep(delay)
		ispy_connection.stop(self.ip_rp)
	
	def Param_Decrease(self,value=30):
		ispy_connection.turn_left(self.ip_rp)
		time.sleep(delay)
		ispy_connection.stop(self.ip_rp)
	
	def copy(self):
		return -1
	
	def paste(self,data):
		return -1
