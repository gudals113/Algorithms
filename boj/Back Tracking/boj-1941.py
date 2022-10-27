# 소문난 칠공주
# hint 220824 - 220829
from collections import deque
from itertools import combinations
G = [input() for _ in range(5)]
answer = 0

def find(node):
    global checked, connected
    x,y = node//5, node%5
    for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
        if 0<=nx<5 and 0<=ny<5 : 
            next = nx*5 + ny
            if next in visitDict and next not in checked:
                checked[next] = 1
                connected+=1
                find(next)
                
def check() :
    #S 개수 체크
    global checked
    global connected
    global visitDict
    connected=0
    checked = {}
    start = visited[0]
    checked[start]=1
    
    visitDict = {}
    for num in visited: visitDict[num]=1    
    find(start)
    
    if connected == 6 :
        return True
    else:
        return False
    
    
answer=0
def DFS(idx, Y, count):
    global answer
    if Y>=4 :
        return
    
    if count == 7:
        if check():
            answer += 1
        return

    for s in range(idx,25):
        sx,sy = s//5, s%5
        
        visited.append(s)
        if G[sx][sy]=='Y': DFS(s+1,Y+1, count+1 )
        else: DFS(s+1,Y, count+1)
        visited.pop()

visited=[]        
DFS(0,0,0)
print(answer)