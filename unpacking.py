coordinates = (1, 2, 3)
# say we wanna perform
# coordinates[0] * coordinates[1] * coordinates[2]
# this is a lengthy code. It will be simlple if we can do x * y * z
# for that we need to assign values to each variables like
# x = coordinates[0]
# y coordinates[1]
# z = coordinates[2]
# instead of these multiple line codes to assign values to each variable , we can do the same using unpacking method like:
x, y, z = coordinates  #python interpreter sees this and assigns the first value of the tuple to first variable , second value
# to second variable and so on...
print(coordinates[0])
print(coordinates[1])
print(coordinates[2])

# this can be done on a list too
list = [10, 11, 12]
a, b, c = list
print(list[0])
print(list[1])
print(list[2])