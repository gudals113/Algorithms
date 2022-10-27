from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    finalDict = defaultdict(int)
    visited = [[ 0 for _ in range(M)]for _ in range(N)]
    
    def DFS(x,y):
        
        visited[x][y]=1
        word = maps[x][y]
        count[word]+=1
        
        for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
            if 0<=nx<N and 0<=ny<M:
                if maps[nx][ny]!='.' and not visited[nx][ny]:
                
                    DFS(nx,ny)

        
    for x in range(N):
        for y in range(M):
            if maps[x][y]!='.' and not visited[x][y]:
                
                count=defaultdict(int)
                DFS(x,y)
                
                                
                tmpW, tmpC = '',0
                for word, cnt in count.items():
                    
                    if cnt>tmpC:
                        tmpW = word
                        tmpC = cnt
                    elif cnt==tmpC:
                        if ord(tmpW) < ord(word):
                            tmpW = word
                
                for word, cnt in count.items():
                    if tmpC > cnt or word==tmpW:
                        finalDict[tmpW]+=cnt
                    
                    else:
                        finalDict[word]+=cnt

    
    finalList = list(finalDict.items())
    finalList.sort(key= lambda x :-x[1])
    answer = finalList[0][1]

    return answer