# search google " python 3 module index" and visit docs.python for python 3
# It shows all the pre built-in functions in python
import random # this random module is not present in any directory of our project. The interpreter knows that
# it is a built-in function

# random function generates random values btw 0 and 1
# randint function genrates random values in whole numbers btw the given limit specified


for i in range(3):
    print(random.random(),"\n")
for i in range(3):
    print(random.randint(10,20))      # Every ime we run this code, we get new random numbers

members = ["john","mary","josh","bob","pranav","vignesh","depp"]
leader = random.choice(members)        # choice() function picks items at random 
print(leader)