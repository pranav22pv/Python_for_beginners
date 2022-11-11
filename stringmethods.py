course = "python for begginers"
uper = 'HI MY name is PRANAV'
print(len(course)) # len is a sting function/method
print(course.upper()) #upper is a string method
print(uper.lower()) # lower is a string method
print(course)     # when a function is linked to a particular datatype , its called as methods
                  # whereas len , print are all general functions unlike string methods like upper or lower
print(course.find('o'))   # returns the index number of the string
print(course.replace('begginers','absolute beginners')) #replaces the given string with other string that we want

# note find and replace are all case sensitive

print('python' in course)
print('Python' in course) # in function returns bool

# find method returns the index of given character but in method finds whether it is present or not . t/f

#course.upper()
#course.lower()
#course.title()
#course.find()
#course.replace()
#'...' in string