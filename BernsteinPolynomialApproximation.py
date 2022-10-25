n = int(input("The length of the array of function values :"))
f = []
for i in range(0,n):
    f.append(float(input("Enter the function value : "))) 
x = float(input("Enter a value between 0 and 1 at which the approximation should be done : "))


def fac(n):        #factorial
    while n >= 0 and int(n) == n:
      f = 1
      i = 1
      while i < n+1:
          f = f*i
          i += 1
      return(f)

def comb(n,k):    #nCk (combination) function
    c = fac(n)/(fac(k) * fac(n-k))
    return(c)
    
def bp(n,k,x):   #Berstein basis polynomials
    b = (comb(n,k))*(x**k)*((1-x)**(n-k))
    return(b)
    
B = 0 
for k in range(0,n):
    B += f[k]*bp(n,k,x)
    
print("The Bernstein polynomial approximation for the given function at ",x," is ",B,".")
        