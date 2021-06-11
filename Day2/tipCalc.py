#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#Tip Calculator

#get the bill from user
bill = input("What is the total bill? R")
#get the number of people
people = input("How many people are there?")
#what % tip do they want to give?
tip = input("what tip % do you want to give? 10, 12, or 15?")

#calculation
billConv = float(bill)
peopleConv = int(people)
tipConv = int(tip )
tipCalc = tipConv / 100 
tipToAdd = billConv * tipCalc

billWithTip = tipToAdd + billConv

finalCalc = (round(billWithTip / peopleConv, 2)) 
#output

print(f"Each people should pay: R{finalCalc}")

