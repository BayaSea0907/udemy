
class Person(object):
  def talk(self):
      print('hi')
      
class Dog(object):
  def run(self):
      print('running dog')
      
# classを二つ継承する
class PersonDog(Person, Dog):
  def __init__(self):
    super().talk()
    super().run()
    
person_dog = PersonDog()

person_dog.talk()
person_dog.talk()
person_dog.talk()
