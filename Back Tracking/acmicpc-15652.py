#N과M (4)
N, M = map(int, input().split())

arr =[]
ans = 0

def DFS() :
    global ans
    
    if ans == M :
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1):
        if arr==[] or arr[-1] <= i :
            arr.append(i)
            ans+=1
            DFS()
            arr.pop()
            ans-=1

DFS()
