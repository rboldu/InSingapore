import xlrd
file_location= '/home/sachith/excel/ex.xlsx'

class sensor_actuator_read():

	def __init__(self):
		workbook=xlrd.open_workbook(file_location)
		sheet=workbook.sheet_by_index(0)

		self.cols=sheet.ncols
		self.rows=sheet.nrows
		self.sens=0
		self.act=0
		self.number_of_sensors=self.rows-1

		self.data=[[sheet.cell_value(r,c) for c in range(self.cols)] for r in range(self.rows)]

	def numSensors(self):
		return self.number_of_sensors

	def sensor2actuator(self,sensor):
		for i in range(self.rows):
			val=self.data[i][0]
			if(val==sensor):
				self.act= self.data[i][1]
		
		if not self.act:
			return 'wrong entry'
		else:
			return 'Actuator of sensor %d : %d'%(sensor,self.act)

	def actuator2sensor(self,actuator):
		for j in range(self.rows):
			val=self.data[j][1]
			if(val==actuator):
				self.sens= self.data[j][0]
		
		if not self.sens:
			return 'wrong entry'
		else:
			return 'Sensor of actuator %d : %d'%(actuator,self.sens)
