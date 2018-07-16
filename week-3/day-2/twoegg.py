def findfloor(input):   
    incrmnt = 13
    currnt = 14
    lmt = 1
    itr = 1
    while(currnt!=input):
        if (currnt>input):
            currnt = lmt
            while(currnt!=input):      
                currnt+=1
                itr+=1
        elif (currnt<input):
            itr+=1
            lmt+=incrmnt+1
            currnt+=incrmnt        
            incrmnt-=1
    print('found the floor in',itr,'iteration')

findfloor(1)
print('---------------------------------')
findfloor(72)
print('---------------------------------')
findfloor(100)
print('---------------------------------')
findfloor(20)
print('---------------------------------')
findfloor(50)
print('---------------------------------')
