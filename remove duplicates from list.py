#list1 = [1,2,3,4,4,5,6,7,7,8]
#len = len(list1)
#list2 = list1.copy()
#list3 = []
#k = 0
#for i in range(len):
#    for j in range(len):
#        if list1[i] == list2[j]:
#            break
#        else:
#            k = list2[j]
#            print(k)
#print(list2)
#left the program in an unsuccessful state


#mosh's solution

numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)