def numtobinary(x):
	l=[]
	while x>1:
		n=x%2
		l.append(n)
		x=x//2
	l.append(x)
	l.reverse()
	return l

def count1(l):
	count=0
	for i in l:
		if i==1:
			count=count+1
	return count

inp=int(input("enter a number: "))
res=[]
for i in range(inp+1):
	l = numtobinary(i)
	c = count1(l)
	res.append(c)
print (res)
