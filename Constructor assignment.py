class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"HI, I am {self.name}")


john = Person("John Smith")
print(john.name)
john.talk()
print("")
print("")


john = Person("John Smith")
john.talk()      # Each object is a different instance of the Person class.

bob = Person("Bob Smith")
bob.talk()


