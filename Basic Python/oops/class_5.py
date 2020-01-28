# access the class attributes
class Dog:
          # class attribute
          species = "animal"
          # instance attribute
          def __init__(self, name, age):
                    self.name = name
                    self.age = age
# instantiate the Dog class
jimmy = Dog("Jimmy", 15)
tommy = Dog("Tommy", 10)

# access the class attributes
print("Jimmy is an {} ".format(jimmy.__class__.species))
print("Tommy is an {} ".format(tommy.__class__.species))





