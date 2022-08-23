# boj-9576.py
# 책 나눠주기
# greedy 
# sol 220729
T = int(input())
for _ in range(T):
    N, M = map(int,(input().split()))
    L = []
    visited = {}
    for _ in range(M):
        s,e = map(int, input().split())
        L.append([e-s, s, e])
    
    L.sort(key= lambda x:(x[2],x[1]))
    
    answer = 0
    for _,s,e in (L):
        for b in range(s,e+1):
            if b in visited :
                continue
            visited[b]=1
            answer+=1
            break

    print(answer)