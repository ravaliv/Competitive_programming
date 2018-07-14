def numtobinary(x):
	l=[]
	while x>1:
		n=x%2
		l.append(n)
		x=x//2
	l.append(x)
	l.reverse()
	return l

def hamming(x,y):
	count=0
	if len(x)<len(y):
		f=len(y)-len(x)
		# print(f)
		for i in range(0,f):
			x.insert(0,0)
	else:
		f1=len(x)-len(y)
		# print (f1)		
		for i1 in range(0,f1):
			y.insert(0,0)
	for i in range(len(x)):
		if x[i]!=y[i]:
			count+=1
	return count

	# print (x)
	# print (y)




l1=[]
l2=[]
n1=int(input("enter a number: "))
n2=int(input("enter a number: "))
l1=numtobinary(n1)
l2=numtobinary(n2)
print (hamming(l1,l2))
# print (l2)



