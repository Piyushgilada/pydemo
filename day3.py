# print("welcome to day 3")

# number=int(input("which number do you want to check?"))
# number1=str(number)
# if number%2==0:
#     print(number1+"\tthis is even number")
# else:
#     print(number1+"\tthis is odd number")

##rollercoaster
# print("welcome to rollercoaster")
# height=int(input("what is yor height in cm?"))
# if height >= 120:
#   print("you can ride")
#   age=int(input("what is your age?"))
#   if age<=18:
#       print("pay rs 10")
#   elif age<=25:
#       print("pay rs 15")
#   else:
#       print("pay rs 20")
# else:
#    print("you can not ride")

## bmi calculator 2.0

# height=float(input("what is your height in meter?"))
# weight=float(input("what is your weight?"))
# bmi=int(weight/height**2)
# bmi1=str(bmi)
# print("your bmi is"+bmi1)
# bmi=int(input("enter your bmi"))
# if bmi<=18:
#     print(f"your bmi is {bmi},your are underweight")
# elif bmi<=24:
#     print(f"your are fit")
# else:
#     print(f"your are fatty")


##leap year
# year=int(input("Enter Which year you want to check?"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("this is a leap year")
#         else:
#             print("this is not leap year")
#     else:
#         print("this is leap year")
# else:
#     print("this is not leap year")


# Rollercoaster updated
# height=int(input("what is yor height in cm?"))
# if height >= 120:
#   print("you can ride")
#   age=int(input("what is your age?"))
#   bill=0
#   if age<=18:
#       bill=10
#       print("pay rs 10")
#   elif age<=25:
#       bill=15
#       print("pay rs 15")
#   else:
#       bill=20
#       print("pay rs 20")
#   want_photo=(input("do you want to take photo ? Y or N"))
#   if want_photo == "Y":
#       bill += 3
#       print(f" final total bill is{bill}")
# else:
#    print("you can not ride")

##pizza order challege
# print("welcome to dominos!!")
# size=str(input("what size do you want for pizza?\nlarge\nmedium\nsmall"))
# if size=="large":
#     bill=300
#     print("cost of pizza is 300")
# elif size=="medium":
#     bill=200
#     print("cost of pizza is 200")
# elif size=="small":
#     bill=100
#     print("cost of pizza is 100")
# add_pepperoni=str(input("do you want to add pepperoni?Y or N"))
# if add_pepperoni=="Y":
#     if size=="small":
#         bill+=20
#         print(f"cost of pizza is {bill}")
#     if size=="medium":
#         bill+=30
#         print(f"cost of pizza is {bill}")
#     if size=="large":
#         bill+=50
#         print(f"cost of pizza is {bill}")
# extra_cheese=str(input("do you want extra cheese?Y or N"))
# if extra_cheese=="Y" :
#     bill+=30
#     print(f"cost of pizza is {bill}")


##love calculator
# print("welcome to love calculator")
# name1=input("what is your name?\n")
# name2=input("what is their name?\n")
# combined_string=name1+name2
# lower_case=combined_string.lower()
# t=lower_case.count("t")
# r=lower_case.count("r")
# u=lower_case.count("u")
# e=lower_case.count("e")
# true=t+r+u+e
# l=lower_case.count("l")
# o=lower_case.count("o")
# v=lower_case.count("v")
# e=lower_case.count("e")
# love=l+o+v+e
# love_score=str(true)+str(love)
# love_score1=int(love_score)
# print(love_score)
# if love_score1>=90:
#     print(f"this is true love with score {love_score}")
# elif love_score1>=50:
#     print(f"this is a love with score {love_score}")
# else:
#     print(f"your love score is {love_score}")


# #final project
# #tresure island
# print("welcome to the tresure island")
# print("your mission is to find tresure !")
# direction=input('you are at a cross road.where do you want to go? type"left"or "right"')
# print(direction)
# if direction=="left":
#     direction1=input("you came across the lake.there is a island in the midddle of the lake.type'wait'to wait for a boat.type'swim' to swim across.")
#     if direction1=="wait":
#         direction2 =input("you arrive at island unharmed.There is house of three doors.one is red,one yellow,and one is blue.which color you want to choose?")
#         if direction2=="red":
#             print("you are dead by fire")
#         elif direction2=="yellow":
#             print("you are safe")
#         else:
#             print("you are dead by water")
#     else:
#         print("you're game over you can't swim far")
# else:
#     print("you are game is over")

# end of day3
