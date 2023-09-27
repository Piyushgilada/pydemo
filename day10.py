# function with output
# def format_name(f_name,l_name):
#   if f_name==""or l_name=="":
#     return
#   else:
#     title_first_name=f_name.title()
#     title_last_name=l_name.title()
#     return f"{title_first_name} {title_last_name}"
# formated_string=format_name(input("what is first name?"),input("What is last name"))
# #storing output in variable and then printing the variable
# print(formated_string)

# def format_name(f_name,l_name):
#   title_first_name=f_name.title()
#   title_last_name=l_name.title()
#   print(f"{title_first_name} {title_last_name}")
# format_name("piyush","GILAdA")                      #calling function

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operation = {"+": add, "-": sub, "*": mul, "/": div}


# making dictionery of operation and key
def calculator():
    num_1 = float(input("What is first number?"))
    for symbol in operation:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("pick any operation from above")
        num_2 = float(input("what is next number?"))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num_1, num_2)
        print(f"{num_1}{operation_symbol}{num_2}={answer}")
        if input("type 'y' to continue calculating with {answer},or type 'n' to exit: ,start new calculation :") == "y":
            num_1 = answer
        else:
            should_continue = False
            calculator()


calculator()
