def inwords(n):
    digits = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
    c = str(number)
    clist = list(c)
    l = len(clist)
    inwords = ''
    for i in range(0,l):
        inwords = inwords + ' ' + digits[clist[i]]
    return (inwords)
number=int(input("Enter the number in figures : "))
print(inwords(number))



