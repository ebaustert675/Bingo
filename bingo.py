import random

def bingo():
    p = random.randint(1,5)
    if(p == 1):
        p = "B"
        n = random.randint(1, 15)
    elif(p == 2):
        p = "I"
        n = random.randint(16, 30)
    elif(p == 3):
        p = "N"
        n = random.randint(31, 45)
    elif(p == 4):
        p = "G"
        n = random.randint(46, 60)
    elif(p == 5):
        p = "O"
        n = random.randint(61, 75)
    out = p + str(n)
    return out


r = bingo()
print(r)
