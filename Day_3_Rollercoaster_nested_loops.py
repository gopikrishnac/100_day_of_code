# Nested Conditions if and else
print("Welcome to the roller coaster ride !!!")
height = int(input("What is your height in cm ? "))

if height > 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry,you have to grow taller before you can ride.")