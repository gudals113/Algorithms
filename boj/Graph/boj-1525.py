# 퍼즐
# BFS
# hint, 220830- 220831
# 메모리 초과가 내부 연산에서 발생했다. 생각보다 메모리초과와 시간 복잡도의 연관이 크다.
# 그래도 좋은 문제라고 생각은 안한다.

from collections import deque
from copy import deepcopy

INF = float('inf')
G = [ list(map(int, input().split())) for _ in range(3)]

visited = {}
start = ''
for x in range(3):
    for y in range(3):
        start += str(G[x][y])

visited[start]=0

q= deque()
q.append(start)
answer = -1
while q :
    strG= q.popleft()
    
    if strG == '123456780':
        answer = visited[strG]
        break
    
    for k in range(9):
        if strG[k]=='0':
            x = k//3
            y = k%3

    for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
        if 0<=nx<3 and 0<=ny<3:                
            copyG = list(strG)
            target = nx*3+ny
            copyG[x*3+y], copyG[target] =copyG[target] , copyG[x*3+y] 
            newStrG = ''.join(copyG)
                    
            if not visited.get(newStrG):
                visited[newStrG]=visited[strG]+1
                q.append(newStrG)

print(answer)