# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

heightConv = float(height)
weightConv = int(weight)

#print(heightConv)
#print(weightConv)

heightCalc = (heightConv * heightConv)

#print(heightCalc)

bmiCalc = weightConv / heightCalc

#print(bmiCalc)

finalAns = int(bmiCalc)
print(finalAns)