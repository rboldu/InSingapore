import sys
from smart_plug import *
ip='192.168.81.1'
port='3480'

switch4 = smart_plug(ip,port)
switch4.setId(4)
switch5 = smart_plug(ip,port)
switch5.setId(5)

switch4.setCategory('Light')

switch4.setOff()

switch4.setOn()

k=switch5.getId()
print k

l=switch4.getStatus()
print l

switch4.setIntensity(20)

switch4.Increase(50)

p=switch4.getIntensity()
print p

j=switch4.getWhoIm()
print j






