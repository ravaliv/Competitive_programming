def myanagram(s1,t1):
    
    l1=list(s1)
    l2=list(t1)
    count=0

    for i in l2:
        if i in l1:
            count=count+1
        else:
            break
    if count==len(l2):
        return 'true'
    
    return 'false'
        



s=input("Enter the first string: ")
t=input("Enter the second string: ")
####print (s)
##print (t)
s1=s.lower().replace(" ","")
t1=t.lower().replace(" ","")
print (myanagram(s1,t1))



