# 이모티콘
# 소트게임 문제 처럼 bfs로 충분히 풀 수 있는 문제다.
# 알았지만 다익스트라로 풀었다.
# 220728 sol
from heapq import heappop, heappush
S = int(input())
INF = float('inf')

def deijkstra():
    heap = []
    heappush(heap, [0,1,0])
    dist = [ [INF for _ in range(2001)] for _ in range(2001)]
    dist[1][0]=0
    
    while heap:
        time, cnt, clip = heappop(heap)
        
        if cnt < 1 or cnt > 1000:
            continue
            
        if cnt+clip > 2000 :
            continue
        
        
        if dist[cnt][clip] < time:
            continue

        
        # print(time, cnt, clip)
        
        if cnt == S:
            print(time)
            break
        
        
        if dist[cnt-1][clip] > time+1:
            dist[cnt-1][clip] = time+1
            heappush(heap, [time+1, cnt-1, clip])

        if dist[cnt][cnt] > time+1 :
            dist[cnt][cnt] = time+1
            heappush(heap, [time+1, cnt, cnt])
        
        if clip != 0:
            if dist[cnt+clip][clip] > time+1:
                dist[cnt+clip][clip] = time+1
                heappush(heap, [time+1, cnt+clip, clip])

deijkstra()
            
       
# INF = float('inf')
# visited = [INF for _ in range(2001)]
# sol = INF
# visited[1] = 0
# def DFS(num, time, clip):
#     global sol
    
#     if clip+num >2000:
#         return
    
#     if time > sol :
#         return
    
#     if num == S:
#         sol = min(sol, time)
    
    
#     for nextnum, nexttime in ([num+clip, time+1], [num-1, time+1]):
#         if visited[nextnum] > nexttime:
#             visited[nextnum] = nexttime
#             DFS(nextnum, nexttime, clip)
            