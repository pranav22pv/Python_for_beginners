message = input(">")
words = message.split(" ")    # we are passing split method with one space i.e " ". so one space is the seperator
#print(words)                      # split method basically spearates words , with given value as boundary, if specified

emojies = {
":)":"😊",
":(":"😔",
"<3":"❤",
"<<3":"❤️"

}

output = ""
for ch in words:
    output += emojies.get(ch,ch) + " "   # get(dictionary_key,default_if_not_found)
print(output)
