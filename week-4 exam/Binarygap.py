

def Binarygap(r):
    count = 0
    while (r!=0):
        r = (r & (r << 1))
        count=count+1
     
    return count
inp=int(input())

print(Binarygap(inp))

