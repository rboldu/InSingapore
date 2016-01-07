import sys
from smart_plug import *
ip='192.168.81.1'
port='3480'

switch4 = smart_plug(ip,port)
switch4.SetID(4)
switch5 = smart_plug(ip,port)
switch5.SetID(5)

switch5.Category()

switch4.ON()

switch5.OFF()