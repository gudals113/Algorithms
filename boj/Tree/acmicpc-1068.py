# 트리
# DFS로 탐색하며 삭제한 노드 나오면 return / tree의 길이가 1인 노드(leaf)가 등장 혹은 길이 2이고 한 쪽이 삭제할 노드면 sol += 1
N= int(input())
parent = list( map(int, input().split() ) )
toDelete = int(input())
tree =[ []for _ in range(N) ]
rootNode = -1

for c in range(N):
    p = parent[c]
    
    if p ==-1:
        rootNode = c
        tree[c].append(-1)
        pass
        
    else :
        tree[c].append(p)
        tree[p].append(c)

visited = [-1 for _ in range(N)]
sol =0
def DFS(node):
    global sol
    visited[node]=1
    
    if node == toDelete :
        return
    
    if len(tree[node]) ==1 or (len(tree[node])==2 and toDelete in tree[node] ) :    
        sol +=1
        return
    
    for child in tree[node]:
        if child != parent[node] and visited[child] ==-1 :
            DFS(child)
        
    return
 
DFS(rootNode)
print(sol)


#DFS로 탐색하며 모두 지우고 길이가 1인 tree 개수 출력하기 (통과 못함)
# from collections import deque

# N = int(input())
# parent = list(  map(int, input().split()) )
# deleted = int(input())

# tree=[[] for _ in range(N)]
# for c in range(N):
#     p = parent[c]
#     if p !=-1:
#         tree[c].append(p)
#         tree[p].append(c)
#     else:
#         tree[c].append(-1)

    
# visited= [-1 for _ in range(N)]
# q=deque([deleted]) 

# if deleted!=0:
#     tree[parent[deleted]].remove(deleted)
#     visited[parent[deleted]] =0
    
# while q:    
#     node = q.popleft()
#     visited[node]=0
#     for child in tree[node]:
#         if visited[child]==-1:# 지워진 노드의 부모 빼고 자식들 다 지웡
#             q.append(child)

#     tree[node]=[]
    
# # print(tree)

    
# sol = 0 
# for i in range(0,N):
    
#     if len(tree[i]) ==1 :
#         sol+=1


# print(sol)