#N과M (3)
N, M = map(int, input().split())

arr =[]
ans = 0

def DFS() :
    global ans
    
    if ans == M :
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1):
        
        arr.append(i)
        ans+=1
        DFS()
        arr.pop()
        ans-=1

DFS()
