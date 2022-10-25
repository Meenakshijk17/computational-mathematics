n = int(input(" Enter the degree of the polynomial : "))
c = []
for i in range(0,n+1):
	c.append(float(input("Enter the coefficients of the terms in ascending order of powers, starting from the constant term : ")))

def f(x):
	f = 0
	for i in range(0,n+1):
		f += c[i]*(x**i)
	return(f)

a = float(input("Enter the lower bound : "))
b = float(input("Enter the upper bound : "))

if a < b:
	N = int(input("Enter the number of subintervals required : "))
	h = (b-a)/N
	s = 0
	a0 = a
	for i in range(0,N):     #lower sum
		a1 = a0+h
		if f(a0) <= f(a1):
			s += f(a0)*h
		else:
			s += f(a1)*h
		a0 = a1
	print("Lower sum = ", s)
	S = 0
	a0 = a
	for i in range(0,N):     #upper sum
		a1 = a0+h
		if f(a0) <= f(a1):
			S += f(a1)*h
		else:
			S += f(a0)*h
		a0 = a1
	print("Upper sum = ", S)
	M = 0
	a0 = a
	for i in range(0,N):   #trapezoidal sum
		a1 = a0+h
		M += (f(a0)+f(a1))*h/2
		a0 = a1
	print("Trapezoidal sum = ", M)

else:
	print("Invalid interval")