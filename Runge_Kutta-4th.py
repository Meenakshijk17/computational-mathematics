"""Runge-Kutta method of 4th order for the differential equation y' = 1+ty , y(0) = 1"""

def f(t,y):
	return(1+t*y)

n = int(input("Enter the step at which the solution value is required : "))
t = []
for i in range(0,n+1):
	t.append(0)
t[0] = 0
y = []
for i in range(0,n+1):
	y.append(0)
y[0] = 1

h = float(input("Enter the step size : "))

for i in range(0,n):
	k1 = h*f(t[i],y[i])
	k2 = h*f(t[i]+h/2,y[i]+k1/2)
	k3 = h*f(t[i]+h/2,y[i]+k2/2)
	k4 = h*f(t[i]+h,y[i]+k3)
	y[i+1] = y[i]+ (1/6)*(k1+(2*k2)+(2*k3)+k4)

print("An approximate value of the solution at the {} -th iteration of Runge - Kutta method is {}".format(n,y[n]))