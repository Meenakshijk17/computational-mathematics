# Note : Due to the availability of only finite sums, the values of log,ln,e^,sin,cos and tan functions may fluctuate widely.

type = input("Binary(Enter B) or Unary(Enter U) : ")
if type == 'B':
    x = float(input("Enter the first operand : "))
    y = float(input("Enter the second operand : "))
    op = input("Enter the operation to be done(+,-,*,/,^,C) : ")
elif type == 'U':
    x = float(input("Enter the operand : "))
    op = input("Enter the operation to be done(1/,!,log,ln,e^,sin,cos,tan) : ")
else:
    print("Invalid type")
    
def fac(n):        #factorial
    while n >= 0 and int(n) == n:
      f = 1
      i = 1
      while i < n+1:
          f = f*i
          i += 1
      return(f)

def comb(n,k):    #nCk (combination) function
    c = fac(n)/(fac(k)*fac(n-k))
    return(c)      
    
def log(x):	      #logarithm to the base 10
	while x > 0:
		l = 0
		y = x-1
		for i in range(1,85):
			l = l+((-1)**(i+1))*(y**i)/i
		return(l)

def ln(x):        #natural logarithm
	y = x-1
	l = 0
	for i in range(1,85):
		l = l+((-1)**(i-1))*(y**i)/i
	return(l)
    
def e(x):   #exponential function
	e = 0
	for i in range(0,85):
		e = e+(x**i)/fac(i)
	return(e)   
    
def sin(x):   #sine function
    s = 0
    for i in range(0,85):
        s = s+(((-1)**i)*(x**((2*i)+1))/fac((2*i)+1))
    return(s)
    
def cos(x):   #cosine function
	c = 0
	for i in range(0,85):
		c = c+((-1)**i)*(x**(2*i))/fac(2*i)
	return(c)
	
def tan(x):    #tan function
	return((sin(x))/(cos(x)))
    

if op == '+':
    print(x,"+",y,"=",x+y)
elif op == '-':
    print(x,"-",y,"=",x-y)
elif op == '*':
    print(x,"*",y,"=",x*y)
elif op == '/':
    print(x,"/",y,"=",x/y)
elif op == '^':
    print(x,"^",y,"=",x**y)
elif op == 'C':
    print(x,"C",y,"=",comb(x,y))
elif op == '1/':
    print("1/",x,"=",1/x)
elif op == '!':
    print(x,"! =",fac(x))
elif op == 'log':
	print('log ',x,'=',log(x))
elif op == 'ln':
	print('ln ',x,'=', ln(x))
elif op == 'e^':
	print('e^',x,'=',e(x))
elif op == 'sin':
	print('sin (',x,')=',sin(x))
elif op == 'cos':
	print('cos (',x,')=',cos(x))
elif op == 'tan':
	print('tan (',x,')=',tan(x))
else:
	print("Invalid operation")