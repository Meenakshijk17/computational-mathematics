m = int(input("Enter the numerator : "))
n = int(input("Enter the denominator : "))

D = [m,]   #list of dividends
d = [n,]     # list of divisors
q = [m//n,]  #list of quotients
r = [m % n,]   #list of remainders

i = 0
while r[i] > 0:
	D.append(d[i])
	d.append(r[i])
	q.append(D[i+1]//d[i+1])
	r.append(D[i+1]%d[i+1])
	print(D[i],'=',q[i],'*',d[i],'+',r[i])
	i += 1
print(D[i],'=',q[i],'*',d[i],'+',r[i])
	