# 이진 검색 트리
# tree
# sol 220910 
import sys
sys.setrecursionlimit(10**5)
L = []
while True:
# for _ in range(9):
    try : L.append(int(input()))
    except EOFError:break
    
N = len(L)
tree = [[-1,-1]for _ in range(N)]

def DFS(root,e):
    left, right = -1, -1
    if root==N-1:
        return
    
    if  L[root] > L[root+1] :
        left = root+1

    for i in range(root+1,e):
        if L[root] < L[i] :
            right = i
            break

    tree[root] = [left,right]
    
    if left!=-1 :
        if right ==-1:
            DFS(left,e)
        else:
            DFS(left,right)
    if right!=-1:
        DFS(right,e)


def post(node):

    left,right  = tree[node]
    
    if left!=-1:
        post(left)
    
    if right!=-1:
        post(right)
        
    print(L[node])

answer=[]
DFS(0,N)
post(0)

    
    
    