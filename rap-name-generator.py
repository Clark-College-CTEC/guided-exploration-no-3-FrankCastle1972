# Guided Exploration No. 3
# YOUR Stew

# Snippet 1
# ================================
# Adding Python Random Library
import random

# Snippet 2
# ================================
# this adds file called Possible_names, to link to the txt file.
possible_names = []

# Snippet 3
# ================================
# this adds a txt file where we will be "writing" the outcome to.
outputFile = open('rap-names-output.txt', 'w')

# Snippet 4
# ================================
# adding snippet #4 which allows us to open and read this txt file.
with open('rap-names.txt', 'r') as dataFile:
    # this looks at the 'dataFile' for "name"
    for name in dataFile:
        # this take to names off of the list and appends them, also stright
        possible_names.append(name.rstrip())

# Snippet 5
# ================================
# asks the question of how many names will we create.
count = int(input('How many rap names would you like to create? '))
# asks how many random names will be put together
parts = int(input('How many parts should the name contain? '))

# Snippet 6
# ================================
# this is where we add a couint of how many name we want to generate.
for i in range(count):
    # this is where the names will be appened to.
    name_parts = []
    # this is the range within parts
    for j in range(parts):
        # name_parts will append from possible_names using random.ramdint
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

# Snippet 7
# ================================
# this is the output function that put a space between words
        outputFile.write(f"{' '.join(name_parts)}\n")
# this is were we print the names
print(f"{' '.join(name_parts)}")

# Snippet 8
# ================================
# this gives us a close out file.
outputFile.close()
