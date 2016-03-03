import xlrd
import re

file_loc='/home/sachith/inSight_excel2/inSight.xlsx'
workbook=xlrd.open_workbook(file_loc)

class Behaviour_excel():
	def __init__(self):
		self.x_cordinate=0
		self.y_cordinate=0
		self.row_number=0

	def selectActuatorAction(self,controller,actuator,control_action):
		sheet=workbook.sheet_by_index(0)

		cols=sheet.ncols
		rows=sheet.nrows

		data=[[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

		for i in range(rows):
			if (data[i][0]==controller):
				x_cordinate=i

		for j in range(cols):
			if (data[0][j]==actuator):
				y_cordinate=j

		behaviour = data[x_cordinate][y_cordinate]
		
		sheet_number=int(re.search(r'\d+', behaviour).group())

		B=workbook.sheet_by_index(sheet_number)

		cols_B=B.ncols
		rows_B=B.nrows
		
		data_B=[[B.cell_value(r,c) for c in range(cols_B)] for r in range(rows_B)]
		
		for i in range(rows_B):
			if (data_B[i][0]==control_action):
				self.row_number=i
		if not data_B[self.row_number][1]:
			print 'wrong entry!'
		else:
			return data_B[self.row_number][1]