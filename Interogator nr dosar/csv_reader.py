import csv
import os
import traceback
from open_dialog import open_file_dialog

# IN = fisier .csv cu numele furnizat de argumentul 'csv_name' (default este export.csv)
# OUT = un array cu toate elemntele csv-ului
# 		(cu exceptie argumentele oprionale 'rows_to_ignore'.
# 		 Ele vor fi pasate ca int-uri , ca argumente aditionale )
# EXEMPLU = csv_to_array('export.csv',1,2,3) -> va importa export.csv si va ignora randurile 1,2,3

def csv_to_array(csv_name='export.csv', *rows_to_ignore):
	csv_array = []
	path = ''
	try:
		with open(str(csv_name), 'r') as csv_file:
			for index, row in enumerate(csv.reader(csv_file)):
				if index not in rows_to_ignore:
					csv_array.append(row)
		csv_file.close()
		path = os.path.abspath(csv_name)

	except IOError:
		path = os.path.abspath(csv_name)
		# print("{} NOT FOUND !".format(path))
		# print("Thrown by :\'{}\'".format(csv_name))
		# print("Switching to manual open dialog ...\n\n")

		with open(open_file_dialog(), 'r') as csv_file:
			for index, row in enumerate(csv.reader(csv_file)):
				if index not in rows_to_ignore:
					csv_array.append(row)
		path = str(csv_file)
		csv_file.close()
	finally:
		return csv_array,path




