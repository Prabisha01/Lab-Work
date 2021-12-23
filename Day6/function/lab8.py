#Python function that takes a number as a parameter and check the number is prime or not. 
def primeCheck(n):
    for i in range(2,n):
        if n % i==0:
            print("Composite")
            break
    else:
        print("Prime")
primeCheck(12)