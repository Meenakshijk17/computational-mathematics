n = int(input("Enter the degree of the polynomial function : "))
a = float(input("Enter the lower bound : "))
b = float(input("Enter the upper bound : "))
N = int(input("Enter the number of subintervals required : "))
c = []
for i in range(0,n+1):
	c.append(float(input("Enter the coefficients of the polynomial in the ascending order of variable power : ")))
def f(x):
	f = 0
	for i in range(0,n+1):
		f += c[i]*(x**i)
	return f
h = (b-a)/N
def trap(a,b,N):
	t = 0
	for i in range(0,N+1):
		x0 = a
		x1 = a+(i*h)
		t += (f(x1)-f(x0))*h/2
		x0 = x1
	print("By Trapezoidal method : ", t)
def Simp1(a,b,N):
	s = f(a)+f(b)
	for i in range(2,N,2):
		x = a+(i*h)
		s += 2*f(x)
	for i in range(1,N,2):
		x = a+(i*h)
		s += 4*f(x)
	s = s*h/3
	print("By Simpson's 1/3-rd rule : ", s)
def Simp2(a,b,N):
	s = f(a)+f(b)
	for i in range(1,N):
		x = a+(i*h)
		if i%3!=0:
			s += 3*f(x)
		else:
			s += 2*f(x)
	s = 3*s/8
	print("By Simpson's 3/8-th rule : ", s)

trap(a,b,N)
Simp1(a,b,N)
Simp2(a,b,N)
	
