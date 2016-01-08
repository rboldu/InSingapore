import urllib2

class Smart_plug_connection():
	
	def __init__(self):
		print 'Working url'
		self.ip='192.168.81.1'
		self.port='3480'

	def setIP(self,ip):
		self.ip=ip

	def setPORT(self,port):
		self.port=port

	def changeIP(self,set_ip):
		self.ip=set_ip

	def changePORT(self,set_port):
		self.port=set_port

	def setOn(self,id):
		http="http://%s:%s/data_request?id=lu_action&output_format=json&DeviceNum=%s&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=1" %(self.ip,self.port,id)
		print http
		#url_response = urllib2.urlopen(http)
 
	def setOff(self,id):
		http="http://%s:%s/data_request?id=lu_action&output_format=json&DeviceNum=%s&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=0" %(self.ip,self.port,id)
		print http
		#url_response = urllib2.urlopen(http)
