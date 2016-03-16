import socket

class dali_connection():
	
	def __init__(self):
		self.ip='192.168.1.250'
		self.port='50000'
		self.version='1'
		self.command='13'
		#self.constant_light='1'
		#self.block='1'
		#self.scene='1'
		self.level='0'
		self.fade_time='1'

	def setIP(self,ip):
		self.ip=ip

	def setPORT(self,port):
		self.port=port

	def setVersion(self,version):
		self.version=version

	def setCommand(self,command):
		self.command=command

	def setConstant_light(self,c_light):
		self.constant_light=c_light

	def setBlock(self,block):
		self.block=block

	def setScene(self,scene):
		self.scene=scene

	def setFade_time(self,fade_time):
		self.fade_time=fade_time

	def changeIP(self,change_ip):
		self.ip=change_ip

	def changePORT(self,change_port):
		self.port=change_port

	def changeVersion(self,change_version):
		self.version=change_version

	def changeCommand(self,change_command):
		self.command=change_command

	def changeConstant_light(self,change_c_light):
		self.constant_light=change_c_light

	def changeBlock(self,change_block):
		self.block=change_block

	def changeScene(self,change_scene):
		self.scene=change_scene

	def changeFade_time(self,change_fade_time):
		self.fade_time=change_fade_time

	def setOn(self,id):
		#command = '>V:%s,C:%s,G:%s,K:%s,B:%s,S:%s,F:%s#' %(self.version,self.command,id,self.constant_light,self.block,self.scene,self.fade_time)
		self.level=100
		command = '>V:%s,C:%s,G:%s,L:%s,F:%s#' %(self.version,self.command,id,self.level,self.fade_time)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip, self.port))
		s.send(command)
		s.close()
 
	def setOff(self,id):
		self.level=0
		command = '>V:%s,C:%s,G:%s,L:%s,F:%s#' %(self.version,self.command,id,self.level,self.fade_time)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip, self.port))
		s.send(command)
		s.close()