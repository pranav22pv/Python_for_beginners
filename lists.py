name = ["john" , "mosh", "sarah" , "bob" , "mary"] # items in the lists shld be inserted inside a square brackets.
print(name)
print(name[0])
print(name[2])
print(name[-2])
print(name[2:]) # [2: ] means starting from index 2 to the end of the list
#print(name[2:4]) # [2:4] means starting from index 2 till one previous the end index, it wont include the end index
print(name[:]) # this returns all elements since it assumes the beginning index as 0
name[0] = "jon"
print(name)