n = int(input("Enter the upper bound : "))
j = int(input("Enter the m value : "))
def divisibility(n,m):
	if n%m == 0:
		return(1)
	else :
		return(0)
		
i = j
while i <= n:
	p = 1
	for k in range(1,j+1):
		p *= divisibility(i,k)
	if p == 1:
		print(i)
		break
	else:
		i  += 1
 		
 	
 			