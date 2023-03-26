#Body Mass Index Calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#BMI Explained - https://en.wikipedia.org/wiki/Body_mass_index
bmi = float(weight) / float(height) ** 2
print(int(bmi))