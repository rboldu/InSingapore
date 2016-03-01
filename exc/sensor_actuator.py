from sensor_actuator_read import*
from sensor_actuator_write import*
file_loc= '/home/sachith/excel/ex.xlsx' 

sensor_actuator_write=sensor_actuator_write(file_loc)
#sensor_actuator_read=sensor_actuator_read()

class sensor_actuator():

	def numSensors(self):
		numSensors=sensor_actuator_read.numSensors()
		print numSensors

	def sensor2actuator(self,sensor):
		actuator=sensor_actuator_read.sensor2actuator(sensor)
		print actuator

	def actuator2sensor(self,actuator):
		sensor=sensor_actuator_read.actuator2sensor(actuator)
		print sensor

	def addNew(self,sensor,actuator):
		sensor_actuator_write.addNew(sensor,actuator)
		print "Successfully added"