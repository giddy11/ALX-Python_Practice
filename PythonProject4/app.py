from PyDictionary import PyDictionary
from computerWords import computer_words, letters_are_in_word, calculate_points, is_word_duplicate
import random, time, threading


dictionary = PyDictionary()
score = 0
word_list = []
start_time = time.time()
max_duration = 50
elapse_time = 0
computer_input = random.choice(computer_words)

def user_input_thread():
    while time.time() - start_time < max_duration:
        global score
        elapsed_time = time.time() - start_time  # Calculate the elapsed time
        
        # if elapsed_time >= max_duration:
        #     print("Maximum time (60 seconds) reached. Stopping the loop.")
        #     break

        print(time.time())
        print("\n{}".format(computer_input))

        user_input = input("Enter a word: ").lower()

        word_tally = letters_are_in_word(computer_input, user_input)

        if word_tally == 1:
            valid_word = dictionary.meaning(user_input)

            if valid_word == 1:
                if not is_word_duplicate(user_input, word_list):
                    word_point = calculate_points(user_input)
                    score += word_point
                    word_list.append(user_input)
                    print("[{}pt(s)]".format(word_point))

input_thread = threading.Thread(target=user_input_thread)
input_thread.start()
input_thread.join(max_duration)

try:
    if input_thread.is_alive():
        print("Maximum time (60 seconds) reached. Stopping the input thread.")
        input_thread._stop()
except AssertionError:
    print("Time up")

print("\nTotal score: {}\nPlease press any key and enter to continue".format(score))