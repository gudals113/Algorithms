#욕심쟁이 판다
# sol220829
# dp
import sys
sys.setrecursionlimit(10**4)

N = int(input())
G = [ list(map(int, input().split())) for _ in range(N) ]

ate = [[0 for _ in range(N)]for _ in range(N)]
answer = 0


def find(x,y):
    
    if ate[x][y] != 0 :
        return ate[x][y]
    
    for nx, ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
        if 0<=nx<N and 0<=ny<N and G[nx][ny]<G[x][y]:
            ate[x][y] = max(ate[x][y], find(nx,ny)+1)ㅇd
    
    return ate[x][y]
    
for x in range(N):
    for y in range(N):
        tmp = find(x,y)
        answer = max(tmp, answer)
        
print(answer+1)