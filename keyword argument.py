def greet_user(firstname,lastname):
    #name= "john"
    print(f"Hi {firstname} {lastname} !")
    print("Welcome aboard")

def lines():
    for i in range(2):
        print("")

print("Start")
greet_user("smith","john")   #arguments are positional arguments meaning they are passed in the order they are positioned
print("Finish")   # if u run this, u can see the name as smith john and not john smith

# however using keyword arguments, position doesn't matter
lines()
print("Start")
greet_user(lastname = "smith",firstname = "john") # having the parameter with its value/ argument is called keyword argument
print("Finish")

#Keyword argument can be useful to increase the readability of the code especially when passing numerical arguments.eg:
# calculate(50,10,0.5)  # this is hard to understand
# calculate(total=50,shipping=10,discount=0.5) # this is easily readable and understandable and code can be used by anyone

# if we are using both positonal argument and keyword argument, keyword argument should be used after positional argument