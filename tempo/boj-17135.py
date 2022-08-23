# 캐슬 디펜스
# 220803
# 구현인데 화나서 그만둠
from itertools import combinations

N,M,D = map( int, (input().split()) )
G = [[ 0 for _ in range(M)]for _ in range(N+1)]

monsterIdx = 0
monsterList = []
for i in range(N):
    l = list(map(int, (input().split())))
    for j in range(M):
        if l[j]==1:
            monsterIdx+=1
            G[i][j] = monsterIdx
            monsterList.append([i,j,monsterIdx])

monsterList.sort(key=lambda x:x[1])

def hunting(y):
    catchDict = {}
    x=N
    distList = [[]for _ in range(41)]
    
    for mx,my in monsterList:
        dist = abs(x-mx) + abs(y-my)
        distList[dist].append([mx,my])
    
    while x>0:    
        catch = 0
        for dist in range(1,41):
            l = distList[dist]
            sortedl = sorted(l, key=lambda x:x[1])
            
            for mx,my in sortedl:
                mIdx = G[mx][my]
                if mx < x and abs(x-mx) + abs(y-my) <= D:
                    if mIdx not in catchDict:
                        catchDict[G[mx][my]]=1
                        catch=1
                        break
            
            if catch==1:
                break
        x-=1
        
    return catchDict

def sumOfThree(x,y,z):
    die ={}
    dx,dy,dz = dictList[x],dictList[y],dictList[z]
    
    for m in dx:
        die[m]=1
        
    for m in dy:
        die[m]=1
        
    for m in dz:
        die[m]=1
        
    return len(die)
      
dictList = []
for i in range(M):
    d = hunting(i)
    dictList.append(d)

answer =0
l = list(combinations([i for i in range(M)],3))
for i,j,k in l:
    tmp = sumOfThree(i,j,k)
    answer = max(answer, tmp)
       
print(answer)