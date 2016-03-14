import socket
import sys

#HOST, PORT = "192.168.1.50", 8888
PORT=8888

FORWARD='1121'
BACKWARD='1222'
LEFT='1021'
RIGHT='1120'
STOP='1020'

command=STOP

class ispy_connection_rp():

	def __init__(self):
		self.ip_rp='Please set the IP of RP'

	def setIP(self,ip):
		self.ip=ip

	def setIP_RP(self,ip_rp):
		self.ip_rp=ip_rp
		#print self.ip_rp

	def setPORT(self,port):
		self.port=port

	def forward(self):
		data='up'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect((self.ip_rp, PORT))
			sock.sendall(data + "\n")
			received = sock.recv(1024)
		finally:
			sock.close()


	def backward(self):
		data='back'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect((self.ip_rp, PORT))
			sock.sendall(data + "\n")
			received = sock.recv(1024)
		finally:
			sock.close()

	def turn_right(self):
		data='right'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect((self.ip_rp, PORT))
			sock.sendall(data + "\n")
			received = sock.recv(1024)
		finally:
			sock.close()	

	def turn_left(self):
		data='left'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect((self.ip_rp, PORT))
			sock.sendall(data + "\n")
			received = sock.recv(1024)
		finally:
			sock.close()

	def stop(self):
		data='stop'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect((self.ip_rp, PORT))
			sock.sendall(data + "\n")
			received = sock.recv(1024)
		finally:
			sock.close()		
