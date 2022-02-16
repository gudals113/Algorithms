#트리
def countTree(N,M):
    global tree, visited, isTree
    count=0    
    tree = [ [] for _ in range(N+1) ]
    
    for _ in range(M):
        nodeA, nodeB = map(int, input().split())
        tree[nodeA].append(nodeB)
        tree[nodeB].append(nodeA)
    
    visited=[ -1 for _ in range(N+1) ]
    for i in range(1,N+1):
        
        if tree[i] == []:
            count+=1
        else:
            if visited[i]==-1:
                visited[i]=1
                isTree=True
                DFS(-1, i)
                if isTree == True:
                    count+=1        
    return count      

def DFS(prev, node): #현재 노드 기준으로 DFS 이미 방문한 노드 나오면 트리 아닌거야!
    global isTree
    for next in tree[node]:
        if visited[next] !=-1 :
            if prev!=-1 and next != prev :
                isTree = False  #전역 변수로 체크하기
        else:
            visited[next]=1
            DFS(node,next)

case=0
while True:
    N,M = map(int, input().split())
    if N ==0 and M == 0 :
        break
    else:
        case+=1
        sol = countTree(N,M)
        if sol==1:
            print(f'Case {case}: There is one tree.')
        elif sol==0:
            print(f'Case {case}: No trees.')
        else:
            print(f'Case {case}: A forest of {sol} trees.')
