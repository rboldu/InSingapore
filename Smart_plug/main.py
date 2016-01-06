import sys
from smart_plug import *
ip='192.168.81.1'

switch4 = smart_plug(ip)
switch4.SetID(4)
switch5 = smart_plug(ip)
switch5.SetID(5)

switch4.ON()

switch5.OFF()