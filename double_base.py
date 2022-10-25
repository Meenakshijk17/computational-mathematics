def reverse(m):
	new_m = []
	for i in range(0,len(m)):
		new_m.append(m[len(m)-(i+1)])
	return(new_m)

def binary(n):
	a = n
	l = []
	while a > 0 :
		b = a%2
		a = a//2
		l.append(b)
	new_l = reverse(l)
	bin = ''
	for i in range(len(new_l)):
		bin += str(new_l[i])
	return(bin)
	
	
def palindrome(n):
	l = list(str(n))
	for i in range(len(l)):
		if l[i] != l[len(l)-i-1]:
			return(0)
			break
	return(1)

n = int(input("Enter the upper bound : "))
for i in range(1,n+1):
	num = i
	bin_num = binary(i)
	if palindrome(num)*palindrome(bin_num) == 1:
		print("{} is a double base palindrome. It's binary correspondant is {}.".format(num,bin_num))
		
		
	