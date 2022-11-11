def square(number):
    print(number*number)

print(square(3))
# By default all functions return the value None. If we dont't have areturn statement in a function, the interpreter by default
# returns None..

def square(number):
    return number*number

print(square(3))   # None won't be returned this time as we have already assigned what to return in the function.

