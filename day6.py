# ##functions
# def my_function():   #defining a function
#     print("hello")   #function is consists of many instruction....
#     print("bye")
#
# my_function()        #calling function
#
#
# ## while loop
# while something_is_true:
#     #do this
#     #then do this
#     #then do this
#
#
# hurdles challenge
# reeborg's world


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    jump()
