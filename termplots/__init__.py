from typing import List


def biground(num, roundto):
    if( num%roundto < roundto/2 ):
        return round(num - (num%roundto), 8)
    else:
        return round(num - (num%roundto) + roundto,8)
      
def find(arr: List, num, ystep ,pos):
    ris = -1
    for x in arr:
        try:
            if(biground(x[pos], ystep)==num and ris != -1):
                ris = len(arr)
            elif(biground(x[pos], ystep)==num):
                ris = arr.index(x)
        except IndexError:
            pass

    return ris
        
def frange(start, stop, step=1.0):
    if(start > stop):
        step *= -1
    curr = start
    tmp = []
    while curr >= stop:
        tmp.append(biground(curr, step))
        curr += step
    return tmp

def plot(iny: List, ystep=1, lowlim=None, highlim=None, car='*'):
    if lowlim == None:
        lowlim = biground(min(iny), ystep)
    if highlim == None:
        highlim = biground(max(iny), ystep)+ 2*ystep
        

    maxLenY = len(str(biground(min(iny), ystep))) if len(str(biground(min(iny), ystep))) > len(str(biground(max(iny), ystep))) else len(str(biground(max(iny), ystep)))

    
    for y in frange(highlim, lowlim, ystep):
        nSpazi = maxLenY - len(str(abs(y)))
        print(f'{" "*nSpazi}{abs(y)}|', end="")
        

        if(y == 0):
            for x in iny:
                if(biground(x, ystep) == y):
                    print(car, end="-")
                else:
                    print("--", end="")
        else:
            for x in iny:
                if(biground(x, ystep) == y):
                    print(car, end=" ")
                else:
                    print("  ", end="")
        print("")


    print()


def mplot(iny: List, ystep=1, lowlim=None, highlim=None, car: List = ['*', '#', '@'], labels:List=None):

    if lowlim == None:
        for serie in iny:
            if(iny[0] == serie):
                mymin = min(serie)
            elif(min(serie) < mymin):
                mymin = min(serie)
            lowlim = biground(mymin, ystep) 
    if highlim == None:
        for serie in iny:
            if(iny[0] == serie):
                mymax = max(serie)
            elif(max(serie) > mymax):
                mymax = max(serie)
            highlim = biground(mymax,ystep) + 2*ystep
            
    for serie in iny:
        if(iny[0]== serie):
            xdim = len(serie)
        elif(len(serie) > xdim):
            xdim = len(serie)

    for serie in iny:
        maxLenY = len(str(biground(min(serie), ystep))) if len(str(biground(min(serie), ystep))) > len(str(biground(max(serie), ystep))) else len(str(biground(max(serie), ystep)))


    for y in frange(highlim, lowlim, ystep):
        nSpazi = maxLenY - len(str(abs(y)))
        print(f'{" "*nSpazi}{abs(y)}|', end="")

       
        if(y == 0):
            for x in range(xdim):
                if(find(iny, y, ystep ,x) != -1):
                    print(car[find(iny, y, ystep ,x)], end="-")
                else:
                    print("--", end="")
            
        else:
            for x in range(xdim):
                if(find(iny, y, ystep ,x) != -1):
                    print(car[find(iny, y, ystep ,x)], end=" ")
                else:
                    print("  ", end="")
        print("")

    print()
        
    if (labels != None):
        for label in labels:
            print(f'{car[labels.index(label)]}: {label}')
        print(f'{car[-1]}: overlaps')


# Tests...
#plot([112, 132, 30], ystep=50)
#plot([0,0.1,0.3], ystep=0.3)
#plot([-32,-20,0,20,32], ystep=10)
#mplot([[-32,-20,0],[32,20,0, 112]], ystep=50)