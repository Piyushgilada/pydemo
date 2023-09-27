# dictionaries
# and
# nesting

# dictionery is denoted by {key :value} pair
# 1) bug an error in a program that prevent the programmer from running as expected
#
# programing_dictionary = {"Bugs":"an error in a program that prevent the programmer from running as expected ",
#                        "Function":"a piece of code that you can easily call over again"}
#
# programing_dictionary["Loop"]="The action of doing something over and over again."    # add loop
# print(programing_dictionary)
# programing_dictionary["Bugs"]="A moth in your computer."                              # edit of bug
# print(programing_dictionary)
# for key in programing_dictionary:
#     print(key)                                                                        # key
#     print(programing_dictionary[key])                                                 # value

# student_score={
#     "Harry":81,
#     "Ron":78,
#     "Hermione":99,
#     "Draco":74,
#     "Neville":62,
# }
# for key in student_score:
#     print(key)
#     print(student_score[key])
#     if student_score[key] in range(91,100):
#         print("Outstanding")
#     elif student_score[key] in range(81,90):
#         print("Exceeds Expectation")
#     elif student_score[key] in range(71,80):
#         print("Aceptable")
#     else:
#         print("Fail")
#     print("\n")


# # nesting dictionary in dictionary
# travel_log={
# "France":{"cities_visited":["Paris","Lille","Dijon"]},
# "Germany":{"cities_visited":["Berlin","Hanburg","Sluttgart"]},
# }
# print(travel_log)
#
# # nesting a dictionary in list
# travel_log=[
#     {"France":"Paris",
#      "Germany":"Berlin"}]
# print(travel_log)

# # dictionary in list
# travel_log=[{
#     "country":"france",
#     "visits":12,
#     "cities":["paris","lille","dijon"]
# },
#     {"country":"germany",
#      "visits":5,
#      "cities":["berlin","hamburg","sluttgart"]},
# ]
# def add_new_country(country_visited,times_visited,cities_visited):
#     new_country={}
#     new_country["country"]=country_visited
#     new_country["visited"]=times_visited
#     new_country["cities"]=cities_visited
#     travel_log.append(new_country)                    # add dictionary in list
# add_new_country("russia",5,["moscow","saint"])        # Calling function
# print(travel_log)


from replit import clear

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with the bid of {bid_amount}")


while not bidding_finished:
    name = input("what is your name? ")
    price = int(input("what is your bid? $"))
    bids[name] = price
    should_continue = input("are there any other bidders? Type'yes'or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
