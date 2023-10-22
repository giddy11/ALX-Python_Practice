import time
import threading

# List of words
word_list = ["able", "on", "them"]

def is_word_duplicate(word, word_list):
    if word in word_list:
        print("A duplicate word was found.")
    else:
        print("No duplicate words found.")

max_duration = 60  # Maximum duration in seconds
start_time = time.time()  # Record the start time

def user_input_thread():
    while time.time() - start_time < max_duration:
        input_word = input("Enter a word (or press Enter to stop): ")
        if input_word == "":
            break
        is_word_duplicate(input_word, word_list)

# Start the user input thread
input_thread = threading.Thread(target=user_input_thread)
input_thread.start()

# Wait for the user input thread to finish, but not more than max_duration
input_thread.join(max_duration)

# Continue with the rest of your program
# ...

# If the user input thread is still running after max_duration, stop it
if input_thread.is_alive():
    print("Maximum time (60 seconds) reached. Stopping the input thread.")
    input_thread._stop()




