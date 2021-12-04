classa=int(input("Enter the number of student of class A :"))
classb=int(input("Enter the number of student of class B :"))
classc=int(input("Enter the number of student of class C :"))
deska=classa//2
deskb=classb//2+classb%2
deskc=classc//2
print(f"The total number of desk is {deska+deskb+deskc}")