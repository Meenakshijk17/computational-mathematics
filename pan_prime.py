def prime(n):
	p = 1
	for i in range(2,int(n/2)+1):
			if n%i == 0:
				p = 0
				break
	return(p)

def pandig(n):
	l = list(str(n))
	p = 1
	for i in range(1,len(l)+1):
		if str(i) not in l:
			p = 0
			break
	return(p)

def pan_prime(n):
	if pandig(n)*prime(n) == 1:
		print(n,"is a pandigital prime.")
	elif pandig(n) == 0 and prime(n) == 0:
		print(n,"is neither pandigital nor prime.")
	elif pandig(n) == 0:
		print(n,"is not pandigital.")
	elif prime(n) == 0:
		print(n,"is not prime.")

n = int(input("Enter the number to be checked : "))

pan_prime(n)