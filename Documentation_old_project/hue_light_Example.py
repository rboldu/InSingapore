#!/Users/issackelly/Projects/python/python-hue/env/bin/python
import sys
sys.path.insert(0, '../Library/')

from hue import Hue
import time

#this clas modify the light

class HueLight():

    
    def __init__(self,id=-1,ip='192.168.1.99',lig='l1'):
        self.h = Hue()
        self.h.station_ip = ip

        self.h.get_state()
  
        self.level=60
        self.status=0
        self.id=id
        self.lig=lig
        self.color=[255,255,255,0,0]
        
        self.h.lights[self.lig].rgb(self.color[0],self.color[1],self.color[2])
        self.h.lights[self.lig].bri(self.level,1)
        self.h.lights[self.lig].off()
    def getId(self):
        return self.id
        #returns the ID
    def getWhoIm(self):
        print "HueLight"
        return "Hue Light"
        #returns what kind of object are
    def changeStatus(self):
        if self.status == 0 :
            self.status=1
            self.h.lights[self.lig].on()
            self.h.lights[self.lig].bri(self.level,1)
        else :
            self.h.lights[self.lig].off()
            self.status=0
        #here is going to change the status of the onject, example ON/OF
    def setIntensity(self,intensity=100):
        self.h.lights[self.lig].bri(self.level,1)
        #Intensity it means like a potenciometer, if I have a light is going to be the brignest of the light
        #de value of the intensity it shoud be between 0 and 255
    def setOn(self):
        self.h.lights[self.lig].on()
        self.status=1
        #Turns on the device
    def setOff(self):
        self.h.lights[self.lig].off()
        self.status=0
        #Turns off the device
    def setParameter(self,parameter=100):
        self.h.get_state()
        #This is going to be a caracteristinc, for example the color of the light also a value between 0 and 255
    def getParameter(self):
        self.h.get_state()
        #retunrs the parameter for example de color if its a light

    def getStatus(self):
        return self.status
    def copy(self):
        aux=[self.color[0],self.color[1],self.color[2],self.status,self.level]
        return aux
        
    def paste(self,data):
        
        if data[3]==1:
            if self.status==0 :
                self.setOn()
                self.status=1
            if data[0]!=-1 and data[1]!=-1 and data[2]!=-1:
                self.color[0]=data[0]
                self.color[1]=data[1]
                self.color[2]=data[2]
                self.color[3]=data[3]
                self.color[4]=data[4]
                self.level=data[4]
                self.updateColor()
                print "pasting intensity tooo to: "+ str ( self.level)
                self.setIntensity()
                print "-------------- I'm pasting----------------\n-------"+str(self.color)+"-------------\n"
                
            else :
                if data[4]!=-1:#audio copy
                    self.level=data[4]
                    self.setIntensity()
                    print "pasting intensity tooo to: "+ str ( self.level)
          
        else :
            self.status=0
            self.setOff()
    def Increase(self,value=40):
        self.level+=value
        if self.level > 255 :
            self.level=255
        self.h.lights[self.lig].bri(self.level,1)
    def Decrease(self,value=40):
        self.level-=value
        if self.level <5 :
            self.level=5
        self.h.lights[self.lig].bri(self.level,1)
        

    def Param_Increase(self,value=10):
        self.color[1]+=value
        self.color[2]-=value
        if self.color[1] >250 :
            self.color[1]=0
        if self.color[2] <0 :
            self.color[2]=250
        self.updateColor()

    def Param_Decrease(self,value=10):
        self.color[2]+=value
        self.color[1]-=value
        if self.color[2] >250 :
            self.color[2]=0
        if self.color[1] <0 :
            self.color[1]=250
        self.updateColor()

    def updateColor(self):
        try:
            self.h.lights[self.lig].rgb(self.color[0],self.color[1],self.color[2])
        except:
            print "colooooooooor errorrrr"



