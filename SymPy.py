from sympy import *

x, y, z = symbols("x y z") # symbolising x, y and z

expr1 = tan(x) + 5 # defining an expression in x
expr1.subs(x,y) # substituting y for x
print(expr1.subs(x,0)) # prints the expression value at 0

expr2 = sin(x) + cos (x)
print(expand_trig(expr2)) # prints the trigonometric expansion of the expression

expr3_str = "x**2 + 3"
expr3 = sympify(expr3_str) # converts string into SymPy expressions

expr4 = sqrt(99)
val = expr4.evalf() # evaluates the square root

print(simplify((x**2 + x)/(x*sin(y)**2 + x*cos(y)**2))) # simplifies the expression
