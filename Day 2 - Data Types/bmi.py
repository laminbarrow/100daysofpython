#Body Mass Index Calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_float = float(height)
bmi = float(weight) / (height_float * height_float)
print(int(bmi))