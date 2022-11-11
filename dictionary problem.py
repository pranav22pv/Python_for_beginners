phone = input("phone: ")
digits_mapping = {
"1":"one",
"2":"two",              # COMMAS ARE VERY IMPORTANT IN BTW EACH KEY
"3" : "three",
"4":"four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + "  "
print(output)