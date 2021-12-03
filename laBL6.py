

#sum of first 10 odd integer


num = range (1, 10)
sum = 0;

for i in range(1, 10):

    if(not (i % 2) == 0):
        sum += i;

print("Sum of odd numbers is :", sum)


