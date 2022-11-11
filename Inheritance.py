# Inheritance is a mechanism for reusing code

#class Dog:
 #   def walk(self):
  #      print("Walk")

#class Cat:
 #   def walk(self):
  #      print("Walk")

# In programming we have a principle called DRY - Don't Repeat Yourself!
# if we repeat the code in many classes and if we find a fault in the code, then we need to change the code in all classes.self
# Another method to do this easily is to create a seperate class and move the walk method there, and will make cat class and
# dog class and every other class to inherit the method . This makes use code reusability . We need not repeat the code for every
# class.

# THIS CAN BE DONE LIKE:

class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):   # by this the dog class will inherit all the methods in Mammal class.
    pass         # Python doesn't like empty class. so we need give any functions or use the keyword pass. tells to pass this nd dw abt this class.

# 2 line breaks after class
class Cat(Mammal):
    pass



class Human(Mammal):
    def annoying(self):      # if we don't pass self argument , it shows TypeError: annoying() takes 0 positional arguments but 1 was given
        print("Annoying")          # Here we don't need the pass statement because we are not leaving the class empty instead
                                   # we create a seperate class exclusively for human class.

# Now we can create a dog or cat object and call funtions from Mammal since dog and cat have inherited Mammal class.
dog1= Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()

human1 = Human()
human1.annoying()

