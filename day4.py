# import random
# random_integer=random.randint(1 , 10)
# print(random_integer)
# random_float=random.random()
# print(random_float)
# random_decimal=random.randint(1,5)
# print(random_decimal)
# love_score=random.randint(50,100)
# print(f"your love score is {love_score}")

# import random
# random_side=random.randint(0,1)
# if random_side==1:
#     print("heads")
# else:
#     print("tails")

# #list
# states_of_america=["Delaware","Pennsylvania","Alabama","Alaska","Arizona"]
# print(states_of_america[-2]) #acess
# states_of_america[1]="pencil" #modify
# print(states_of_america)
# states_of_america.append("aditya") #append
# print(states_of_america)
#
#
# import random
# name_string=input("give me everyone's names,separated by a comma.")
# name=name_string.split(",")
# num_item=len(name)
# random_choice=random.randint(0,num_item-1)
# person_who_will_pay=name[random_choice]
# print(person_who_will_pay+"is going to buy meal today")

# tresure map(nested list)
# row1=["😃","🤨","😙"]
# row2=["🤬","😠","☺️" ]
# row3=["🥴","🤬","😠"]
# map=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position=input("where do you want to put the tresure?")
# horizontal=int(position[0])
# vertical=int(position[1])
#
# selected_row=map[vertical-1]
# selected_row[horizontal-1]="x"
# print(map[vertical-1])

#
# user_choice=int(input("What do you want to choice ? type 0 for rock,1 for paper or 2 for scissor\n"))
# print(f"you chossen{user_choice}")
# computer_choice=random.randint(0,2)
# print(f"computer chosen{computer_choice}")
# print(computer_choice)
# if computer_choice==2 and user_choice==0:
#     print("user win!")
# elif computer_choice==user_choice:
#     print("draw!!")
# elif computer_choice==1 and user_choice==2:
#     print("user win!")
# elif computer_choice == 1 and user_choice ==0 :
#     print("computer win!")
# elif computer_choice == 0 and user_choice == 1:
#     print("user win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("computer win!")
# else:
#     print("computer win")
