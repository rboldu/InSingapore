import socket
ip='192.168.1.250'
port='50000'
#cluster/router/subnet/device >>>>>s1.250.2.device
self.ip='192.168.1.250'
port='50000'
version='1'
command='11'
constant_light='1'
block='1'
scene='1'
fade_time='1'


self.scene=16
command = '>V:%s,C:%s,G:%s,K:%s,B:%s,S:%s,F:%s#' %(version,command,group,constant_light,block,scene,fade_time)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((self.ip, self.port))
s.send(command)
s.close()