from ispy_tank import *

ip_rp1='192.168.1.51'
ip_rp2='192.168.1.50'

ispy_2 = ispy_tank(ip_rp2,id=2)
ispy_1 = ispy_tank(ip_rp1,id=1)

ispy_2.setOn()
ispy_1.setOn()
ispy_2.setOn()
ispy_1.setOn()

ispy_1.getId()
ispy_2.getId()




