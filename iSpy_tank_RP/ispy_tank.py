from ispy_connection_rp import *
import time
delay=0.5

ispy_connection=ispy_connection_rp()

class ispy_tank():
	def __init__(self,ip,port,ip_rp,id):
		self.ip=ip
		self.port=port
		self.ID=id
		self.ip_rp=ip_rp
		ispy_connection.setIP(self.ip)
		ispy_connection.setPORT(self.port)
		ispy_connection.setIP_RP(self.ip_rp)

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
		time.sleep(delay)
		ispy_connection.stop()
		#print self.ip_rp

	def setOff(self):
		ispy_connection.stop()
	
	def setParameter(self,parameter):
		return -1
	
	def getParameter(self):
		return -1
	
	def getStatus(self):
		return -1
	
	def Increase(self,value=30):
		ispy_connection.forward()
		time.sleep(delay)
		ispy_connection.stop()
	
	def Decrease(self,value=30):
		ispy_connection.backward()
		time.sleep(delay)
		ispy_connection.stop()
	
	def Param_Increase(self,value=30):
		ispy_connection.turn_right()
		time.sleep(delay)
		ispy_connection.stop()
	
	def Param_Decrease(self,value=30):
		ispy_connection.turn_left()
		time.sleep(delay)
		ispy_connection.stop()
	
	def copy(self):
		return -1
	
	def paste(self,data):
		return -1
