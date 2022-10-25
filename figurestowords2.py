n = int(input("Enter a number less than 100 crores in figures : "))
c = list(str(n))
l = len(c)

o = {'0':'','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
t = {'00':'','01':'One','02':'Two','03':'Three','04':'Four','05':'Five','06':'Six','07':'Seven','08':'Eight','09':'Nine','10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen','20':'Twenty','30':'Thirty','40':'Forty','50':'Fifty','60':'Sixty','70':'Seventy','80':'Eighty','90':'Ninety'}
s = {'2':'Twenty','3':'Thirty','4':'Forty','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}

def p12(x): #regarding the one's and ten's places
	p1 = x[-1]
	p2 = x[-2]
	ties = p2+p1
	if ties in t:
		w = t[ties]
	else:
		w = s[p2] + ' ' + o[p1]
	return(w)
	
def p03(x): #regarding the 3rd place
	p3 = x[-3]
	if p3 == '0':
		return('')
	else:
		return(o[p3] + ' Hundred ')

def p04(x): #regarding 4th place
	p4 = x[-4]
	w = o[p4] + ' Thousand ' + p03(x) + p12(x)
	return(w)
	
def p45(x): #regarding the 4th and 5th places
	ties = x[-2]+x[-1]
	p3 = x[-3]
	p4 = x[-4]
	p5 = x[-5]
	thou = p5+p4
	if thou in t:
		if thou != '00':
			w = t[thou] + ' Thousand ' + p03(x) + p12(x)
		else:
			w = t[thou] + p03(x) + p12(x)
	else:
		w = s[p5]+' '+ o[p4] +  ' Thousand ' + p03(x)+ p12(x)
	return (w)
	
def p06(x): #regarding the 6th place
	p6 = x[-6]
	w = o[p6] + ' Lakh ' + p45(x)
	return(w)

def p67(x): #regarding the 6th and 7th places
	ties = x[-2]+x[-1]
	p3 = x[-3]
	p4 = x[-4]
	thou = x[-5]+x[-4]
	p6 = x[-6]
	p7 = x[-7]
	lakh = p7 + p6
	if lakh in t:
		if lakh != '00':
			w = t[lakh] + ' Lakh ' +  p45(x)
		else:
			w = t[lakh]  +  p45(x)
	else:
		w = s[p7] +' '+ o[p6]+ ' Lakh ' + p45(x)
	return (w)

def p08(x): #regarding the 8th place
	p8 = x[-8]
	w = o[p8] +' Crore ' + p67(x)
	return(w)
	 
def p89(x): #regarding the 8th and 9th places
	ties = x[-2]+x[-1]
	p3 = x[-3]
	p4 = x[-4]
	thou = x[-5]+x[-4]
	p6 = x[-6]
	lakh = x[-7]+x[-6]
	p8 = x[-8]
	p9 = x[-9]
	cr = p9+p8
	if cr in t:
		w = t[cr] + ' Crore ' + p67(x)
	else:
		w = s[p9]+' '+ o[p8]+' Crore ' + p67(x)
	return(w)

if l == 1:
	if n == 0:
		w = 'Zero'
	else:
		w = o[c[0]]
elif l == 2:
	w = p12(c)
elif l == 3:
	w = p03(c) + p12(c)
elif l == 4:
	w = p04(c)
elif l == 5:
	w = p45(c)
elif l == 6:
	w = p06(c)
elif l == 7:
	w = p67(c)
elif l == 8:
	w = p08(c)
elif l == 9:
	w = p89(c)
else:
	w = " Invalid input. Enter a number from 0 to 99,99,99,999."

print(w)