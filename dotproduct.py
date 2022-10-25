n = int(input("Enter the size of the tuples : "))
a = []
b = []
for i in range (0,n):
	a.append(float(input("Enter the first tuple entries one by one : ")))
for i in range (0,n):
	b.append(float(input("Enter the second tuple entries one by one : ")))

def dotproduct(x,y):
	while len(x) == len(y):
		l = len(x)
		d = 0
		for i in range (0,l):
			d += x[i]*y[i]
		return(d)

print("The dot product of ",a," and ", b, " is ", dotproduct(a,b))