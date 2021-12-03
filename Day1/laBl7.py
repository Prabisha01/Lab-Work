#sum of first ten even integer

number = range (1, 11)

sum =0,

for i in range (1, 11):
     if(not ( i % 2) == 0):
             sum += i;

print("Sum of even numbers is :", sum)
