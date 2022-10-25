n = int(input("Enter the length of the vectors : "))
x = []
y = []
for i in range(0,n):
	x.append(float(input("Enter the first vector's coordinates one by one :  ")))
for i in range(0,n):
	y.append(float(input("Emter the second vector's coordinates one by one : ")))
c = 0
for i in range(0,n):
	c += x[n-1-i]*y[i]
print("The convolution of the vectors, ",x , y," is x*y =" , c)
	