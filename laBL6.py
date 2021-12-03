#sum of first 10 odd integer


num = range (1, 20)
sum = 0;

for i in range(1, 20):

    if(not (i % 2) == 0):
        sum += i;

print("Sum of odd numbers is :", sum)


