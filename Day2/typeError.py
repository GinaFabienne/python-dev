#Type error, Type checking and Type conversion
#you will get an error for the following:
#num_char = len(input("What is your name?"))
#print ("Your name has " + num_char + " characters.")

#above will give an error so the check you can use:
#print(type(num_char))
#this will check the type of data - and it will be an integer
#to solve this can use type conversion or type casting to change one data type to another. 
#do this by:
#num_char = len(input("What is your name?"))
#new_num_char = str(num_char)
#print ("Your name has " + new_num_char + " characters.")

#can also convert complex lines like this:
#a = float(123)
#print(type(a))

#print(70 + float("100.5"))
#therefore use the type function to check the data type, then use str, float, int to convert the data to the correct type. 