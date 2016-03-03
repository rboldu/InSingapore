from ispy_tank import *

ip='10.10.1.1'
port=8150

ispy_1 = ispy_tank(ip,port,id=1)

k=ispy_1.getWhoIm()
print k
