import socket
import sys

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

	def forward(self,ip_rp):
		data='up'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect((ip_rp, PORT))
			sock.sendall(data + "\n")
			received = sock.recv(1024)
		finally:
			sock.close()

	def backward(self,ip_rp):
		data='back'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect((ip_rp, PORT))
			sock.sendall(data + "\n")
			received = sock.recv(1024)
		finally:
			sock.close()

	def turn_right(self,ip_rp):
		data='right'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect((ip_rp, PORT))
			sock.sendall(data + "\n")
			received = sock.recv(1024)
		finally:
			sock.close()	

	def turn_left(self,ip_rp):
		data='left'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect((ip_rp, PORT))
			sock.sendall(data + "\n")
			received = sock.recv(1024)
		finally:
			sock.close()

	def stop(self,ip_rp):
		data='stop'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect((ip_rp, PORT))
			sock.sendall(data + "\n")
			received = sock.recv(1024)
		finally:
			sock.close()		
