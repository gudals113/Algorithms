#문자열게임 2
T=int(input())
for _ in range(T):
    TC = input()
    K = int(input())
    
    L = [ [] for _ in range(26)]
    
    minSol = 10001
    maxSol = -1
    for i in range(len(TC)):
        num = ord(TC[i])-97
        
        L[num].append(i)
        
        if len(L[num]) >=K :
 
            minSol = min(minSol, L[num][-1] - L[num][-K] +1 )
            maxSol = max(maxSol, L[num][-1] - L[num][-K] +1)

    if minSol==10001 or maxSol ==-1:
        print(-1)
    else:
        print(minSol, maxSol)