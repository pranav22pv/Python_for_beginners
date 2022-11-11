for item in 'python':
    print(item)
print('')
# in python we can define lists in square brackets . []

for tem in ['john','spidy','voldy']:
    print(tem)
print('')
for em in [1,2,3,4,5,6]:
    print(em)

# we cannot write list of number when n is large , so we have a built in fucntion called range
# range (n) from 0 to n-1
# range (n,m) start from n and go till m-1
# range (n,m,0) 0 means incremnting value.
print('')
for item in range(10):
    print(item)
print('')
for item in range(5,10):
    print(item)
print('')
for item in range(1,11,2):
    print(item)

print('')
price = [10,20,30]
sum = 0
for i in price:
    sum += i
print(sum)