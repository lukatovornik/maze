import random

def narisi_labirint(mreza):
    for  vrsta in mreza:
        for celica in vrsta:
            if celica == 3:
                print("_|", end="")
            elif celica == 2:
                print("_ ", end="")
            elif celica == 1:
                print(" |", end="")
            elif celica == 0:
                print("  ", end="")
        print("")


def generiraj_labirint(mreza):
    '''for n in range(10):
        for m in range(10):
            mreza[n][m]=int(random.random()*4)'''
    končaj=True
    x=0
    y=0
    c=0
    while končaj:
        mreza[x][y]=int(random.random()*2)+1 
        print(x," ",y," ",mreza[x][y])
        if mreza[x][y] == 1:
           x+=1
        elif mreza[x][y] == 2:
            y+=1
        c+=1
        if c ==10:
            končaj=False
        
        
mreza=[[3 for i in range(10)]for j in range(10)]

generiraj_labirint(mreza)
narisi_labirint(mreza)


'''for j in range(10):          
    for i in range(10):
        a=int(random.random()*3)
        #print(a, end='')
        if a==0: 
            print("_", end='')
        elif a==1:
            print(" |", end='')
        elif a==2:
            print("_", end='')
            print("| ", end='')
    print("\n")'''
