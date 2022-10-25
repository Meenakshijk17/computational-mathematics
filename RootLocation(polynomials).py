from math import*
print("Locating a real root, within a given boundary, of any given polynomial using bisection method")

d=int(input("Enter the degree of the polynomial : "))

print("When prompted, enter the coeffients of each term in the polynomial, in the ascending order, starting from the constant term.")

c=[] #list in which the coefficients will be saved
for i in range(0,d+1):
	coeff = float(input("Enter coefficient : "))
	c.append(coeff)

def f(x):  #defining the function
	s = 0
	for i in range(d+1):
		s = s + (float(c[i])*(x**i))
	return(s)
	
a = float(input("Enter the lower bound : "))
b = float(input("Enter the upper bound : "))
	
if f(a)*f(b) >= 0:
	print("We cannot locate a root by this method since the values of the polynomial at both the bounds are of the same sign (in this case, the polynomial might not have a real root at all) or one among them itself is a root (try redefining the bounds)." )
else:
	p = (a+b)/2
	n = 0
	print(" n-------a_n-------b_n-------p_n-------f(p_n)")
	print(n,"---",round(a,5),"---",round(b,5),"---",round(p,5),"---",round(f(p),5))
	while abs(f(p)) > 0.0001:
		n = n+1
		if f(p)*f(b) > 0:
			b = p
		elif f(p)*f(a) > 0:
			a = p
		p = (a+b)/2
		print(n,"---",round(a,5),"---",round(b,5),"---",round(p,5),"---",round(f(p),5))
		
	print("An approximate root of the polynomial(with an error of +/-0.001) was located at ",p," using ",n,"iterations.")
