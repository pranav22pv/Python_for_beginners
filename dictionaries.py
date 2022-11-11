# within a curly braces , we deifne a dictionary
customer = {
"name":"john smith",
"age":30,
#"age":40,  we can't have same key twice..
"is_verified":True
}

print(customer["name"])  # we can access each item in the dictionary using square brackets with "" around the key
# key are sensitive keywords, we can't enter a key that doesn't exist. it will throw an error



# DIFF BTW NORMAL PRINT AND GET() METHOD:
#print(customer["phone"])
print(customer.get("phone"))  # get mthd won't throw error if we enter a key that doesn't exist. it shows as none
# if we need to print any specific value if the user enters a key that doesn't exist , we can do that by
print(customer.get("email","default value"))

# we can easilly add key value pairs into a dictionary
customer["birthdate"] = "Jan 1"  # here instead of :  we use =

print(customer["birthdate"])