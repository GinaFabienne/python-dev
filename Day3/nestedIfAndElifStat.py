#nested if/else

# if condition:
#   if another condition:
#        do this
#    else:
#        do this
# else:
#    do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))


if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    
    if age < 12:
        print("Your ticket price is R10")
    elif age <= 18:
        print("Your ticket price is R20")
    else: 
        print("Your ticket price is R30")
else:
    print("Sorry, you have to grow taller before you can ride.")

