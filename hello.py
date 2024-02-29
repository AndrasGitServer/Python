import random

print('Hello World!')

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(number):
    return random.randint(1, number)

file_is = get_file_ext('t.yes')

print(file_is)
print(roll_dice(8))

