# Write a program to check the Leap Year?
year = int(input("Enter the Year: "))

# it means divided by 100 means century years (ending with 00)
# century year is divided by 400 is leap yrs
if (year % 400 == 0) and (year % 100 == 0):
    print("This is a leap year".format(year))
# not divided by 100 is not a century year
# year is divided by 4 is a leap year
elif (year % 4== 0) and (year % 100 != 0):
    print("This is a leap year".format(year))
#if not didided by 400 both century and leap )
# is not leap year
else:
    print("This not a leap year")

