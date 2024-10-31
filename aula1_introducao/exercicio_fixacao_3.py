#program_name: calculate the amount of change after buying something
#author: gabriel_takiguchi(sidewinder)
#data: 06/03/24
#version: 1.0
#content: simple variable types, algorithm thinking and calculations

value = float(input("item_value:"))
money_delivering = float(input("money_delivering:"))

change = value - money_delivering

print("item_value:",value)
print("money:",money_delivering)
print("change:",change)