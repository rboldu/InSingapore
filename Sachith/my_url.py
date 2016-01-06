import urllib2

def on():
    url_response = urllib2.urlopen('http://192.168.81.1:3480/data_request?id=lu_action&output_format=json&DeviceNum=4&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=1')

def off():
    url_response = urllib2.urlopen('http://192.168.81.1:3480/data_request?id=lu_action&output_format=json&DeviceNum=4&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=0')