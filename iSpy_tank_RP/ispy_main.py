from ispy_tank import *

ip='10.10.1.1'
port=8150

ip_rp1='192.168.1.51'
ip_rp2='192.168.1.50'

ispy_1 = ispy_tank(ip,port,ip_rp1,id=1)
ispy_1.setOn()

ispy_2 = ispy_tank(ip,port,ip_rp2,id=1)
ispy_2.setOn()

