from collections import deque
from copy import deepcopy


def solution(info, edges):
    global answer
    answer = 0
    N = len(info)
    allSheep = info.count(0)
    allWolf = N-allSheep
    
    tree =[[] for _ in range(N)]
    myP = [-1 for _ in range(N)]
    for p, c in edges:
        tree[p].append(c)
        myP[c] = p

    visited = [ 0 for _ in range(N)]
    
    def DFS(node, sheep, wolf, canReach):
        global answer

        answer = max(answer, sheep)
        
        for child in tree[node]:
            canReach[child]=1
        
        
        for next in canReach:
            if not visited[next]:
                if info[next]==0:
                    visited[next]=1

                    newReach = deepcopy(canReach)
                    del newReach[node]
                    DFS(next, sheep+1, wolf, newReach)

                    visited[next]=0
                    
                elif info[next]==1 and sheep > wolf+1 :
                    visited[next]=1
                    newReach = deepcopy(canReach)
                    del newReach[node]
                    DFS(next, sheep, wolf+1, newReach)
                    
                    visited[next]=0
                    
                    
    d = {0:1}    
    visited[0]=1
    for child in tree[0]:
        d[child]=1
    DFS(0,1,0,d)
    print(answer)
    return answer
solution([0,0,1,1,1,0,1,0,1,0,1,1]	,[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])