import urllib2

class url():
	
	def __init__(self):
		print 'Working url'

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
		url_response = urllib2.urlopen(http)
 
	def setOff(self,id):
		http="http://%s:%s/data_request?id=lu_action&output_format=json&DeviceNum=%s&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=0" %(self.ip,self.port,id)
		url_response = urllib2.urlopen(http)
