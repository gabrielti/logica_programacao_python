#program_name: calculate an N number of pavements building area
#author: gabriel_takiguchi(sidewinder)
#data: 06/03/24
#version: 1.0
#content: simple variable types, algorithm thinking and calculations

lenght = float(input("terrain_lenght:"))
width = float(input("terrain_width:"))
number_of_pavements = float(input("number_of_pavements:"))

area = lenght * width * number_of_pavements 

print("area:",area)