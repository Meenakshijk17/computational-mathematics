def matrix(m,n):     #to enter a matrix data
	x = []
	for i in range(0,m*n):    #collects all the entries 
		x.append(float(input(" Enter the matrix entries one by one, row-wise : ")))
	
	A = []
	for i in range(0,m*n,n):   #arranges the entries into rows and columns
		A.append(x[i:i+n])
	return(A)
	
def dotproduct(x,y):      #dot product for matrix multiplication
	while len(x) == len(y):
		l = len(x)
		d = 0
		for i in range(0,l):
			d += x[i]*y[i]
		return(d)
		
def transpose(A,m,n):    #transpose of a matrix
	t = []
	At = []
	for j in range(0,n):
		for i in range(0,m):
			t.append(A[i][j])
	for i in range(0,n*m,m):
		At.append(t[i:i+m])
	return(At)

op = input("Matrix operation to be done ( + if Matrix Addition, . if Scalar Multiplication and * if Matrix Multiplication : ")

if op == '+' :        #matrix addition
	print('First matrix : ')
	m1 = int(input(" Number of rows of the matrix : "))
	n1 = int(input(" Number of columns of the matrix : "))
	print('Second matrix : ')
	m2 = int(input(" Number of rows of the matrix : "))
	n2 = int(input(" Number of columns of the matrix : "))
	if m1 == n1 and n1 == n2:
		print('First matrix : ')
		A = matrix(m1,n1)
		print('Second matrix : ')
		B = matrix(m2,n2)
		y = []
		S = []
		for i in range(0,m1):
			for j in range(0,n1):
				y.append(A[i][j]+B[i][j])
		for i in range(0,m1*n1,n1):
			S.append(y[i:i+n1])		
		print('The sum of the matrices is : ',S)	
	else:
		print("Addition of two matrices of different sizes is not defined.")

elif op == '.':     	#scalar multiplication	
	m = int(input(" Number of rows of the matrix A : "))
	n = int(input(" Number of columns of the matrix A : "))
	A = matrix(m,n)
	c = float(input(" The scalar, c, to be multiplied : "))
	y = []
	SM = []
	for i in range(0,m):	
		for j in range(0,n):
				y.append(c*A[i][j])
	for i in range(0,m*n,n):
			SM.append(y[i:i+n])
	print("The required product is cA =", SM)

elif op == '*':
	print('First matrix : ')
	m1 = int(input(" Number of rows of the matrix : "))
	n1 = int(input(" Number of columns of the matrix : "))
	print('Second matrix : ')
	m2 = int(input(" Number of rows of the matrix : "))
	n2 = int(input(" Number of columns of the matrix : "))
	if n1 == m2:
		print('First matrix : ')
		A = matrix(m1,n1)
		print('Second matrix : ')
		B = matrix(m2,n2)
		Bt = transpose(B,m2,n2)
		y = []
		P = []
		for i in range(0,m1):
			for j in range(0,n2):
				y.append(dotproduct(A[i],Bt[j]))
		for i in range(0,m1*n2,n2):
			P.append(y[i:i+n2])
		print(" The product of the given matrices is : " , P, " which is of size : ",m1,"*",n2)
	else:
		print('Multiplication not defined. The number of columns of the first matrix should be equal to the number of rows of the second matrix.')
		
else:
	print("Undefined operation")