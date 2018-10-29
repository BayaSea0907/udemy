import csv

class CsvController:

	def __init__(self, file_name: str, field_names: list):
		self._file_name = file_name	
		self._field_names = field_names

		try:
			self._csv_file = open(self._file_name, 'a+')

		except Exception as error:
			print('--- Error: csv_file open ---')
			print('message', error)
			print('-----------------------')

	def write(self, row_dict: dict):
		try:
			self.seek(0, 2)
			writer = csv.DictWriter(self._csv_file, fieldnames = self._field_names)
			writer.writerow(row_dict)

			return True

		except Exception as error:
			print('--- Error: csv_file write ---')
			print('message:', error)
			print('-----------------------')
		
			return False

	def reader(self):
		if self._csv_file != None:
			self.seek(0, 0)
			return csv.DictReader(self._csv_file)
		else:
			return None

	# start... 0: 最初 1: 現在地: 2: 最後
	def seek(self, offset: int, start: int):
		self._csv_file.seek(offset, start)


	def show_data(self):
		for row in self.reader():
			print(row)

	def data_count(self):
		self.__counter = 0
		for row in self.reader():
			self.__counter += 1
		return self.__counter

	def __del__(self):
		if self._csv_file != None:
			self._csv_file.close()

