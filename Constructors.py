class Point:
    def __init__(self,x,y):    #Constructor
        self.x = x       # Constructor is a function that gets called at the time of creating an object
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point = Point(10,20)
#point.x
print(point.x)
print(point.y)

point.x = 11   # Can change the value of the parameters anywhere in the program using the object
print(point.x)