'''

phone = input("Phone: ")
digits_map = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
}

for ch in phone:
    print("{} ".format(digits_map.get(ch, "Nah")), end="")
    
'''

'''
message = "Good morning sir :) :( "
word_list = message.split(" ")

emojis = {
    ":)": "😊",
    ":(": "😥"
}

for ch in word_list:
    print("{} ".format(emojis.get(ch, ch)), end="")

'''

