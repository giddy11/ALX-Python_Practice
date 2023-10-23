class DogNameError(Exception):

    def __init(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dog name: ")

    if any(char.isdigit() for char in dogName):

        raise DogNameError
    
except DogNameError:
    print("Your dogs name can't contain a number")