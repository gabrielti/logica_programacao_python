#program_name: calculate a persons aproximate age based on the year their born
#author: gabriel_takiguchi(sidewinder)
#data: 06/03/24
#version: 1.0
#content: simple variable types, algorithm thinking and calculations

year_born = int(input("year_born:"))
current_year = int(input("current_year:"))

age = current_year - year_born

print("aproximate_age:",age)
print("aproximate_months:",age*12)
print("aproximate_days",age*12*365) 

#aproximado por causa do mes, a pessoa ainda vai fazer ou realmente ja fez a idade calculada
#casting