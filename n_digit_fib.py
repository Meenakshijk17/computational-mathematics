def fib(n):
	f = [1,1,]
	for i in range(2,n):
		new = f[i-2] + f[i-1]
		f.append(new)
	return(f[n-1])
leng = int(input("Enter the length of the Fibonacci digit : "))
i = 2
while i >= 2:
	if len(str(fib(i))) == leng:
		print("The first {}-digit Fibonacci number occurs as the {}-th term in the series.".format(leng,i))
		break
	else:
		i += 1
