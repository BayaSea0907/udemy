import csv_controller

class Roboter(object):
	
	def __init__(self, name):
		self.name = name

		# CSV initialize
		self._field_names = ['Name', 'Restaurant', 'FavoCount']
		self.__csv_ctl = csv_controller.CsvController('restaurant_list.csv', self._field_names)


		# data initialize
		self.username = ''
		self.new_restaurant = ''

		self.__row_dict = {}
		for field in self._field_names:
			self.__row_dict[field] = ''
	@classmethod
	def want_input_response(cls, message = ''):
		print(message)
		input()

	@classmethod
	def str_present(cls, message: str):
		if message == '':
			return False
		else:
			return True
	
	def start_up(self):
		if not self.__section1():
			return False		
		if not self.__section2():
			return False
		if not self.__section3():
			return False
		if not self.__section4():
			return False
		
		return True
	
	# 名前を尋ねる
	def __section1(self):
		Roboter.want_input_response('....。')
		Roboter.want_input_response('.............。')
		Roboter.want_input_response('...........................。')

		print('...ナヲナノレ。\n')
		self.username = input('>> ')
		print('\n......', self.username, '。')
		Roboter.want_input_response()

		if Roboter.str_present(self.username):			

			# 既に回答済みの場合は処理を終了
			for row in self.__csv_ctl.reader():
				if row['Name'] == self.username:
					print('...オマエ モウイイ')
					return False

			print('....オデハ ', self.name, '。')
			Roboter.want_input_response()
			return True
		else:
			print('ハナシニナラヌ...。')
			return False


	# レストランをお勧めする
	def __section2(self):
		for row in self.__csv_ctl.reader():
			Roboter.want_input_response('.....。\n')

			print('...オデノ オススメ')
			Roboter.want_input_response()
			print('...【', row['Restaurant'], '】。')
			Roboter.want_input_response()

			print('...オマエモ スキカ? [N/Y]\n')
			flg = input('>> ')
			Roboter.want_input_response()

			if flg == 'Y' or flg == 'y':
				row['FavoCount'] = str(int(row['FavoCount']) + 1)
				# TODO: 更新が出来ぬ

				print('...ワガッタ。\n')

			elif flg == 'N' or flg == 'n':
				print('...ワガッタ。\n')

			else:
				Roboter.want_input_response('... オシエテ クレナイ。')
		return True

	# 好きなレストランを聞く
	def __section3(self):
		Roboter.want_input_response('.......。')
		Roboter.want_input_response('........................。')

		# TODO: 2回まで繰り返して、ダメなら起こる
		print(self.username, 'ノ オススメ オシエロ\n')
		self.new_restaurant = input('>> ')
		print('\n')

		Roboter.want_input_response('...。')
		Roboter.want_input_response('.......。')
		Roboter.want_input_response('........................。\n')

		# 好きなレストランの回答の反応
		if Roboter.str_present(self.new_restaurant):
			print('.....【', self.new_restaurant, '】。')
			Roboter.want_input_response()
			print('...カンシャ。\n')
			return True
		else:
			print('..... ガッカリダ。')
			return False

	# データセーブ
	def __section4(self):
		if (Roboter.str_present(self.username) and Roboter.str_present(self.new_restaurant)):	
			self.__row_dict['Name'] = self.username
			self.__row_dict['Restaurant'] = self.new_restaurant
			self.__row_dict['FavoCount'] = 0
			return self.__csv_ctl.write(self.__row_dict)
		else:
			return False
