class Person(object):
	name = 'BayaSea'

	def who_are_you(self):
		return self.name

	@classmethod
	def class_method_test(cls):
		return cls.name


a = Person()
b = Person

print('a.who_are_you= ', a.who_are_you())
# print('b.who_are_you= ', b.who_are_you())


print('a.name= ', a.name)
print('b.name= ', b.name)

print('a.test= ', a.class_method_test())
print('b.test= ', b.class_method_test())
