#find the factor of number

n = int(input("enter the number: "))
for i in range(1,n+1): 
	if not n%i: 
		print(i,end=' ') 