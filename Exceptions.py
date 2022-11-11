# We use try and except blocks to tackle exceptions and avoid the program from crashing

#age= int(input("Enter the age: "))
#print(age)
# If we enter any a string instead of number in the input , we get a ValueError and program crashes.


try:
    age= int(input("Enter the age: "))
    income = 2000
    risk = income/age
    print(age)
except ValueError:      # value error arises when incompatible value is entered. here it is string since age can't be a string
    print("Invalid value")
except ZeroDivisionError:    # ZeroDivisionError arises when our code tried to divide zero. i.e when user enters zero follishly
    print("Age cannot be zero")

# As a good programmer we must anticipate all the probabilities for the program to crash and must write code for all the possible
# errors that might arise .