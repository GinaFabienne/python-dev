# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#variables
divideBy4 = year % 4
divideBy100 = year % 100
divideBy400 = year % 400

#print(divideBy4)
#print(divideBy100)
#print(divideBy400)

#Code

if divideBy4 == 0:
    print("leap year")
    
