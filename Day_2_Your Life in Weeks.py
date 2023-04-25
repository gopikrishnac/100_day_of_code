# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# if we have left if we live until 90 years old
rest_years = 90-int(age)
# calculating days
x = rest_years * 365
# calculating weeks
y = rest_years * 52
# calculating days
z = rest_years * 12
# print the output using f-strings
print(f"You have {x} days,{y} weeks, and {z} months left.")
