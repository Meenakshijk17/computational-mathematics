n = int(input("Enter the number (positive integer) : "))

def reverse(m):
	new_m = []
	for i in range(0,len(m)):
		new_m.append(m[len(m)-(i+1)])
	return(new_m)

a = n
l = []
while a > 0 :
	b = a%2
	a = a//2
	l.append(b)
	
new_l = reverse(l)

print("The binary number corresponding to {} is : ".format(n))
for i in range(len(new_l)):
	print(new_l[i],end='')




	
	
	