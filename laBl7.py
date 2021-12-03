#sum of first ten even integer

number = range (1, 20)

sum =0,

for i in range (1, 20):
     if(not ( i % 20) == 0):
             sum += i;

print("Sum of even numbers is :", sum)
