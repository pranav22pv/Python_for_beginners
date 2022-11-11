numbers = [2,46,8,4,6,34,53]
print(numbers)
print('')
numbers.append(20) # append an item at the end of the list
print(numbers)
print('')
numbers.insert(0, 10) # insert(index, item)
print(numbers)
print('')
numbers.remove(2)  # removes the specified item from the list
print(numbers)
print('')
numbers.clear()  # clears all items in the list and makes it empty
print(numbers)
print('')
numbers = [2,46,8,4,6,34,8,53]
numbers.pop()  # removes the last item in the list
print(numbers)
print('')
print(numbers.index(6)) # index method returns the index number of the first occurence of the specified item
print(numbers.index(34))  # shows error if item not present
print(50 in numbers)  #returns boolean values acc to the condition if present or not
print('')
print(numbers.count(8))  #returns the number of time the given item is present in the list
print('')
numbers.sort()  # sorts the items in the list in ascending order
print(numbers)
print('')
numbers.reverse()  # sorts the items in the list in descending order
print(numbers)
print('')
numbers2 = numbers.copy()  #copies all the contents in the list
numbers2.append(10)
print(f'{numbers2} {numbers}')