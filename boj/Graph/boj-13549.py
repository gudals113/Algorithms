#숨바꼭질 3 bfs sol220628
#백트래킹을 항상 쓰려고 하면 안된다.
#똑같은거 방문하는 걸 처리할 수가 없어
# import sys
# sys.setrecursionlimit(10**5)
# N, K = map(int,input().split())
# def DFS(place, time):
#     global answer
    
#     if place>K:
#         answer = min(answer, time+ place-K)
#         return 
    
#     if place == K :
#         answer = min(answer, time)
#         return
    
    
#     if place!=0:
#         DFS(place*2, time)

#     if time+1 <= answer:
#         if place-1>0:
#             DFS(place-1, time+1)
#         if place+1<100000:
#             DFS(place+1, time+1)
    
# if K<N :
#     answer = N-K
# else:
#     answer = K-N
#     DFS(N,0)
    
# print(answer)

from collections import deque

N,K = map(int, input().split())
q=deque()
q.append([N,0])

visited=[float('inf') for _ in range(100001)]
visited[N]=0

if K<N :
    answer = N-K
else:
    answer = K-N
    while q:
        place, time = q.popleft()
        
        if place>=K :
            answer = min(answer, place-K+time)        
            continue
        
        if time>=answer:
            continue        
        
        for next_place, next_time in ([place*2, time],[place+1, time+1],[place-1, time+1]):
            if 0<=next_place<100001 and visited[next_place] > next_time:
                visited[next_place] = next_time
                q.append([next_place, next_time])

print(answer)