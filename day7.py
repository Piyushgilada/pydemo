# #goals
# for and while loops
# if /else
# lists
# strings
# range
# module

# game?

import random

list = ["camel", "babboon", "ardvark", "gorilla"]
# //creating list
chosen_word = random.choice(list)
print(f"chosen word is {chosen_word}")
length = len(chosen_word)
display = []
for _ in chosen_word:
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess_letter = input("guess a letter!").lower()
    for position in range(length):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
print(" you win")
