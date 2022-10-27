N = int(input())
tree = [[-1,-1] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(N):
    node,left,right = map(int, input().split())
    tree[node] = [left,right]
    if left!=-1:
        visited[left]=1
    if right!=-1:
        visited[right]=1
    
for node in range(1,N+1):
    if not visited[node]:
        root = node
        break
    
L = [[] for _ in range(N+1)]
P = [0 for _ in range(N+1)]
childNum = [[0,0] for _ in range(N+1)]


def DFS(node):

    left, right = tree[node]
    leftNum, rightNum = 0,0
    
    if left!= -1:
        leftNum = DFS(left)

    if right!=-1:
        rightNum = DFS(right)
    
    if left==-1 and right ==-1:
        return 1    
    
    childNum[node]= [leftNum,rightNum]
    return 1+leftNum+rightNum

def setNum(node,s,e,level):
    left, right = tree[node]   
    leftNum,righrNum = childNum[node]
    P[node] = s+leftNum
    L[level].append(P[node])
    
    if left!=-1:
        setNum(left,s,P[node]-1, level+1)
    
    if right!=-1:
        setNum(right,P[node]+1,e,level+1)
        
def getAnswer():
    answer = [0,0]
    for level in range(1,N+1):
        if len(L[level])==0:
            break
        w = L[level][-1] - L[level][0] + 1
        if answer[1]<w:
            answer = [level,w] 
    
    return answer

DFS(root)
setNum(root,1,N,1)
a = getAnswer()
print(a[0], a[1])