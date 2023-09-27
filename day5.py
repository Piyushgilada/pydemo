# fruits=["apple","peach","pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+" pie")

# student_height=input("input a list of student height").split()
# for n in range(0,len(student_height)):
#     student_height[n]=int(student_height[n])
# print(student_height)
# total_height=0
# ## replace sum function by for loop
# for height in student_height:
#     total_height+=height
# print(total_height)
# ## replace len function by for loop
# number_of_student=0
# for student in student_height:
#     number_of_student+=1
# print(number_of_student)
# ## average of list
# average=total_height/number_of_student
# print(average)
#
# student_height=input("input a list of student height").split()
# for n in range(0,len(student_height)):
#     student_height[n]=int(student_height[n])
# print(student_height)
#
# max_height=0
# for height in student_height:
#     if height>max_height:
#         max_height=height
# print(f"the highest height of student is\t{max_height}")


# total=0
# for number in range(1,101):
#     if number%2==0:
#         total+=number
# print(total)

## fizz buzz project
# for number in range(0,101):
#     if number%3==0 and number%5!=0:
#         print("fizz")
#     elif number%5==0 and number%3!=0:
#         print("buzz")
#     elif number%3==0 and number%5==0:
#         print("fizzbuzz")
#     else:
#         print(number)


##password genarator
import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
          'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '~']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print("welcome to the pypasword genrator!")
nr_letter = int(input("How many letters you want to introduce in your password\n"))
nr_symbol = int(input("how many symbol you want to generate in your password\n"))
nr_number = int(input("how many number you want in password\n"))
password = " "
for char in range(1, nr_letter + 1):
    password += random.choice(letter)
for char in range(1, nr_symbol + 1):
    password += random.choice(symbol)
for char in range(1, nr_number + 1):
    password += random.choice(number)
print(password)
