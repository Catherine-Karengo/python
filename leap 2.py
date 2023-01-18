print("LEAP YEAR OR NOT APP")
print("--------------------")

for x in range(3):
    print("1. Enter a year")
    year = int(input()) #Get input form user

 
    #if year % 4 == 0 or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0): 
    #if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0): 
        print("This is a leap year")
    else:   
        print("Not a leap year")

