def emoji_converter(message):
    words = message.split(" ")
    #print(words)

    emojies = {
    ":)":"😊",
    ":(":"😔",
    "<3":"❤",
    "<<3":"❤️"

    }

    output = ""

    for ch in words:
        output += emojies.get(ch,ch) + " "
    return output

# 2 lines should be left after a function defintion
message=input(">")
print(emoji_converter(message))