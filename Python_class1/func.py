def convert_to_emoji(mess):
    word_list = message.split(" ")

    emojis = {
        ":)": "😊",
        ":(": "😥"
    }
    output = ""
    for ch in word_list:
        output += emojis.get(ch, ch) + " "
    return output


message = "Good morning sir :) :( "
res = convert_to_emoji(message)

print(res)