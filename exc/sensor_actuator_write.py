from xlutils.copy import copy
from xlrd import *
from sensor_actuator_read import*

sensor_actuator_read=sensor_actuator_read()

class sensor_actuator_write():

	def __init__(self,file_loc):
		self.file_loc=file_loc
		self.position=sensor_actuator_read.numSensors()+1
		self.workbook = copy(open_workbook(self.file_loc))

	def addNew(self,sensor,actuator):
		self.workbook.get_sheet(0).write(self.position,0,sensor)
		self.workbook.get_sheet(0).write(self.position,1,actuator)
		self.workbook.save(self.file_loc)