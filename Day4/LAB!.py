#Check whether the given year is leap year or not 
#If year is leap print ‘LEAP YEAR’ 
#else print common year

Year = int(input("enter the year: "))

if ((Year % 400 ==0) or
    (Year % 100 !=0 ) and
    (Year % 4 == 0)):
    print ("The year is leap year")

else:
    print("The year is not ")