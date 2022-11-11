def greet_user(name):    # parameters -> recieve information to a function
    #name= "john"      # a local variable like this is not necessary with parameters
    print(f"Hi {name} !")
    print("Welcome aboard")


print("Start")
greet_user("john")    # so when a function has a parameter, we are obligated to pass a value to the parameter
greet_user("Mary")    # without passing value to the parameter if u try to call function like greet_user() -> THROWS ERROR
print("Finish")       # PARAMETERS are the holes or placeholders that we define in a function to recieve the information
                      # ARGUMENT is the actual piece of information that we supply these functions or
                      # information that we pass while callng a function.. name -> parameter. john,mary -> arguments

#  WE CAN PASS MULTIPLE ARGUMENTS
def greet_user(firstname,lastname):
    #name= "john"
    print(f"Hi {firstname} {lastname} !")
    print("Welcome aboard")


print("Start")
greet_user("john","smith")
print("Finish")