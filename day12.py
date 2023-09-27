# ##############        scope     ###############
# # Local scope /variable
# # global scope/variable
# # there is no block scope
# enemies=1
# def increase_enemies():
#     enemies=2
#     print(f"enemiesinside a function: {enemies}")
#     return enemies
# increase_enemies()
# print(f"enemies outside the function: {enemies}")
#
# #    global constant
# PI=3.14159
# URl="http://www.google.com"


# final project of the day


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    global turns
    level = input("Choose difficulty type 'easy' or 'hard':")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print(f"you got a right guess {guess}")


def game():
    print("         #      Welcome to the number gussing game:      # ")
    from art import logo
    print(logo)
    from random import randint
    answer = randint(1, 100)

    print("I'm thinking of a number between 1 and 100.")
    print(f"correct ans :{answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempt left to guess the number.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you loose you cant guess the number")
            return
        elif guess != answer:
            print("guess again")


game()
