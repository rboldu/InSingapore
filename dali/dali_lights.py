from dali_connection import *

dali_connection=dali_connection()

class dali_lights():
	def __init__(self,dali_ip,dali_port,id):
		self.id=id
		self.ip=dali_ip
		self.port=dali_port
		self.intensity=0
		dali_connection.setIP(self.ip)
		dali_connection.setPORT(self.port)

	def getId(self):
		print self.id

	def getWhoIm(self):
		return 'Dali lights'

	def setGroup(self,group):
		self.group=group

	def getStatus(self):
		return self.status

	def changeStatus(self):
		if (self.status == 1):
			self.setOff()
		else:
			self.setOn()

	def setIntensity(self,intensity):
		self.intensity=intensity

	def getIntensity(self):
		return self.intensity

	def setParameter(self,parameter):
		self.parameter=parameter

	def getParameter(self):
		return self.parameter

	def setOn(self):
		dali_connection.setOn(self.id)
		self.status = 1
		
	def setOff(self):
		dali_connection.setOff(self.id)
		self.status = 0

	def changeIP(self,ip):
		dali_connection.changeIP(ip)

	def changePORT(self,port):
		dali_connection.changePORT(port)

	def changeVersion(self,version):
		dali_connection.changeVersion(version)

	def changeCommand(self,command):
		dali_connection.changeCommand(command)

	def changeConstant_light(self,c_light):
		dali_connection.changeConstant_light(c_light)

	def changeBlock(self,block):
		dali_connection.changeBlock(block)

	def changeScene(self,scene):
		dali_connection.changeScene(scene)

	def changeFade_time(self,fade_time):
		dali_connection.changeFade_time(fade_time)

	def Param_Increase(self,value=30):
		self.intensity=self.intensity+value
		if self.intensity>255:
			self.intensity=255
		self.setOn()
		self.status = 1

	def Param_Decrease(self,value=30):
		self.intensity=self.intensity-value
		if self.intensity<0:
			self.intensity=0
		self.setOff()
		self.status = 0

	def Increase(self):
		self.intensity=self.intensity+5
		if self.intensity>255:
			self.intensity=255
		self.setOn()
		self.status = 1

	def Decrease(self):
		self.intensity=self.intensity-5
		if self.intensity<0:
			self.intensity=0
		self.setOff()
		self.status = 0

	def copy(self):
		return -1
	
	def paste(self,data):
		return -1
