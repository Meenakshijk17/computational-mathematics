tri = set()
pent = set()
hex = set()
n = int(input("Enter the number of elements required : "))
for i in range(1,n+1):
	t = i*(i+1)/2
	tri.add(int(t))
	p = i*(3*i -1)/2
	pent.add(int(p))
	h = i*(2*i -1)
	hex.add(int(h))
print("The first {} triangular numbers are : {}.".format(n,tri))
print("The first {} pentagonal numbers are : {}.".format(n,pent))
print("The first {} hexagonal numbers are : {}.".format(n,hex))

common = tri & pent & hex
print("The numbers in the above lists that are triangular, pentagonal and hexagonal are : ",common)