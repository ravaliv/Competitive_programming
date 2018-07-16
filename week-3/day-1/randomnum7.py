import random

def rand5():
    return random.randint(1, 5)

def rand7():
    roll = 5*rand5()+rand5()-5
    if(roll<22):
        return roll%7 + 1
    return rand7()

print('After rolling a 7 sided die')
print(rand7())
