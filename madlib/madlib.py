import random
adjective = input("Adjective : ")
verb = input("Verb : ")
noun = input("Noun : ")

one = f"Once upon a time, {adjective} [noun] decided to {verb} through the {adjective} forest, where they encountered a {noun} who offered them {adjective} {noun}."
two = f"In a {adjective} {noun}, a group of {noun} embarked on a quest to find the legendary {noun}, but they were hindered by a {adjective} {noun} that {verb} in their path."
three = f"As {adjective} as a summer day, {noun} strolled down the {adjective} {noun}, enjoying the {adjective} scenery until they stumbled upon a {adjective} {noun} that {verb} with curiosity."

madlibs = [one, two, three]

choice = random.choice(madlibs)

print(choice)