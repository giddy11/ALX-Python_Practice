

def letters_are_in_word(word, word2):
    for letter in word2:
        if letter not in word:
            return 0
    return 1


def is_word_duplicate(word, word_list):
    return word in word_list


def calculate_points(word):
    points_dict = {
        2:   1,
        3:   2,
        4:   3,
        5:   4,
        6:   5,
        7:   6,
        8:   7,
        9:   8,
        10:  9,
        11:  10,
        12:  11
    }
    
    word_length = len(word)
    
    return points_dict.get(word_length, 0)  # Return the point value for the word length, default to 0 if not found


computer_words = [
    "international",
    "politicians",
    "pollutions"
]