# Convert temperatures to and from celsius, fahrenheit.

c = float(input("Enter the temperature in celius: "))
f = (c* 9/5) + 32
print("The celcius : {} Farenheit  ". format(f))

f = float(input("Enter the temperature in celius: "))
c = (c -32)* 5/9
print("The celcius : {} Farenheit  ". format(c))