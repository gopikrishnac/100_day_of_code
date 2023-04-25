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