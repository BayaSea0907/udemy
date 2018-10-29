
import abc

class Person(metaclass=abc.ABCMeta):
	
	def __init__(self):
		print('person init')	

	@abc.abstractmethod
	def hoge(self):
		print('hoge')


class Baby(Person):
	pass

class Adult(Person):
	def hoge(self):
		print('im adult')

# baby = Baby()
#=> エラーになります

adult = Adult()
adult.hoge()
