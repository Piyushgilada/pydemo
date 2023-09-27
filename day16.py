#
# from turtle import Turtle,Screen
# timmy=Turtle()
# print(timmy)
# print("str")
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# timmy.shape("turtle")
# timmy.color("cyan")

# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("Pokemon Name",["Pikachu","Squirtle","charmander"])
# table.add_column("Type",["Electric","Fire","Water"])
# table.add_row(["Piyush","Ice"])
# print(table)


from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
money_machine.report()
coffee_maker.report()