import urllib2

ip_add='192.168.81.1'
port='3480'

def changeIP(set_ip):
	ip_add=set_ip

def changeIP(set_port):
	port=set_port

def on(id):
	http="http://%s:%s/data_request?id=lu_action&output_format=json&DeviceNum=%d&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=1" %(ip_add,port,id)
	url_response = urllib2.urlopen(http)
 
def off(id):
    http="http://%s:%s/data_request?id=lu_action&output_format=json&DeviceNum=%d&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=0" %(ip_add,port,id)
    url_response = urllib2.urlopen(http)
