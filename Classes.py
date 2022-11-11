# Naming convention for class:  (naming convention for classes is diff from variables and functions)
# Unlike variable or funtions, we don't use lowercase letters starting or use underscore to seperate multiple words in the name
# Instead we use uppercase letter for the first letter of the name of a class and use uppercase for first letters of every single
# word in the name of class... eg .. variable -> email_client. class -> EmailCLient

class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


#object is an instance of a class. The class defines the cluprint or temlpate to create an object and onjects are the
# actual instances based on the blueprint
# To create an onject we type the name of the class and call it like a function. and store it to a variable name
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()  # This object is completely different from the above object
#print(point2.x)   # this throws an error
point2.y = 1
print(point2.y)
point1.move()



# 2 blank lines should be given before as well as after the class definition.