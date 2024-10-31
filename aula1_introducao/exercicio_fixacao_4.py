#program_name: calculate the tip from a service
#author: gabriel_takiguchi(sidewinder)
#data: 06/03/24
#version: 1.0
#content: simple variable types, algorithm thinking and calculations

service_price = float(input("service_price:"))
tip_percentage = float(input("tip_percentage:"))

money_delivering = (service_price*tip_percentage)/100

print("tip:",money_delivering)
