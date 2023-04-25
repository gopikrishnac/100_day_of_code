# Welcome note
print("Welcome to the tip Calculator.")
# Asking the total bill which in flaot datatype
total_bill = float(input("What was the total bill? $ "))
# How much percentage of tip you wii give? which in integer datatype
tip_percentage = int(input("What percentage tip would you like to give? 10,12,,or 15? "))
# how many people went which in integer datatype
total_people = int(input("How many people to spilt the bill? "))
# calculating the total pay with tip percentage by all people which is in float datatype
total_persons_pay = (total_bill+(total_bill * tip_percentage/100))
each_person_pay = round(total_persons_pay/total_people,2)
print(f"Each person should pay: ${each_person_pay} ")