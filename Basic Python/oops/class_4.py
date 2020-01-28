# access the instance attributes
class Dog:
          # instance attribute
          def __init__(self, name, age):
                    self.name = name
                    self.age = age
# instantiate the Dog class
jimmy = Dog("Jimmy", 15)
tommy = Dog("Tommy", 10)


# access the instance attributes
print("{} is {} years old".format( jimmy.name, jimmy.age))
print("{} is {} years old".format( tommy.name, tommy.age))
