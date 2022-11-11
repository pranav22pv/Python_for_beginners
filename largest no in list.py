# my soln
list = [1000,1234,6726,8926,80,10000,29837,28937,123,1]
length = (len(list))
largest_no = 1
for i in range(length):
    if list[i-1] > list[i] and list[i-1] > largest_no:
        largest_no = list[i-1]
print(largest_no)


#mosh's soln

list = [1000,1234,6726,8926,80,10000,29837,28937,123,1]
max = list[0]
for i in list:
    if i > max:
        max = i
print(max)