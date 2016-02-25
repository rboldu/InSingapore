import socket

FORWARD='1121'
BACKWARD='1222'
LEFT='1021'
RIGHT='1120'
STOP='1020'

command=STOP

class ispy_connection():

	def setIP(self,ip):
		self.ip=ip

	def setPORT(self,port):
		self.port=port

	def forward(self):
		command=FORWARD
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip,self.port))
		s.send(command)
		s.close()

	def backward(self):
		command=BACKWARD
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip,self.port))
		s.send(command)
		s.close()

	def turn_right(self):
		command=RIGHT
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip,self.port))
		s.send(command)
		s.close()	

	def turn_left(self):
		command=LEFT
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip,self.port))
		s.send(command)
		s.close()

	def stop(self):
		command=STOP
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip,self.port))
		s.send(command)
		s.close()		