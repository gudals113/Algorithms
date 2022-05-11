from collections import deque


def solution(places):
    answer = []
    
    
    def BFS(G):    
        for x in range(5):
            for y in range(5):
                if G[x][y] == 'P' :
                    visited= [ [-1 for _ in range(5)] for _ in range(5)]
                    
                    q=deque()
                    q.append([x,y,0])
                    visited[x][y]=0
                    while q:
                        x,y,d = q.popleft()
                        if d == 2:
                            continue
                        
                        for nx,ny in ([x,y+1],[x,y-1],[x+1,y],[x-1,y]):
                            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==-1:
                                if G[nx][ny] == 'O' :
                                    visited[nx][ny] = visited[x][y] + 1
                                    q.append([nx,ny, visited[nx][ny]])
                                
                                elif G[nx][ny] == 'P' :
                                    if visited[x][y] <= 1 :
                                        print(x,y)
                                        return 0
        
        
        return 1
    # BFS(["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"])  
    for G in places:
        sol = BFS(G)
        answer.append(sol)
    
    return answer


solution(["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"])