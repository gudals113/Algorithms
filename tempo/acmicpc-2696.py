#중앙값 구하기 우선 순위 큐
from heapq import heapify, heappop
def main():
    M = int(input())
    if M%10==0:
        caseNum = M//10
    else:
        caseNum = M//10 +1
    
    full = []
    for _ in range(caseNum):
        full+=(list(map(int, input().split())))
    
    sol=[]
    for i in range(0,len(full), 2):
        arr = full[:i+1]
        heapify(arr)
        
        mid = (len(arr)+1)//2
        
        tmp=0
        for _ in range(mid):
            tmp = heappop(arr)
            
       
        sol.append(tmp)
    
    S=len(sol)
    setNum=S//10
    remainidx = (S%10)*-1
    print(S)
    for i in range(setNum):
        print(*sol[i*10:i*10+10])
    if remainidx!=0:
        print(*sol[remainidx:])

T= int(input())
for _ in range(T):
    main()
   