import random

def rand7():
	return random.randint(1,7)

def rand5():
	r = rand7()
	return r if r<=5 else rand5()

print ('Rolling 5-sided die...')
print (rand5())