# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# converting height into float
h = float(height)
# converting weight into integer
w = int(weight)
# calculating BMI
BMI = (w/(h**2))
# print the value of bmi after converting into whole number
print(int(BMI))

if BMI < 18.5:
    print(f"You BMI is {BMI},you are underweight")
elif BMI < 25:
    print(f"You BMI is {BMI},you have a normal weight")
if BMI < 30:
    print(f"You BMI is {BMI},you are slightly overweight")
if BMI < 35:
    print(f"You BMI is {BMI},you are obese")
else:
    print(f"You BMI is {BMI},you are clinically obese")