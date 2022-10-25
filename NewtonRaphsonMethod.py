"polynomials with complex roots will display 100 iterations, in which case, the method fails to locate the root"
from math import*

n = int(input("Enter the degree of the polynomial function : "))
c = []
for i in range(0,n+1):
	c.append(float(input("Enter the coefficients of the polynomial in the ascending order of variable power : ")))
def f(x):  #defining the polynomial function
	f = 0
	for i in range(0,n+1):
		f += c[i]*(x**i)
	return f
def df(x): #derivative of the f(x)
	df = 0
	for i in range(0,n):
		df += (i+1)*c[i+1]*(x**i)
	return df
	
x0 = float(input("Enter the initial approximation of the root : "))
y = x0+1
m = 0
print("n----------xn----------f(xn)")
while(abs(y-x0) > 0.001 and m <= 100):
	print(m,"----------",round(x0,4),"------",round(f(x0),8))
	m += 1
	x = x0-(f(x0)/df(x0))
	y,x0 = x0,x
print(" The number of iterations is {}. The approximate root is {} and the value of the function at the root is {}.".format(m-1,x0,f(x0)))
