# 구간 합 구하기
# sol 220831
# 세그먼트 트리
import math
L = []
INF = float('inf')
N,M,K = map(int, input().split())
for _ in range(N) : L.append(int(input()))
leafNum = math.ceil(math.log2(N))
leafNum = 2**leafNum
nodeNum = leafNum*2 

tree = [ 0 for _ in range(nodeNum)]
for i in range(N):
    leaf = leafNum + i
    tree[leaf] = L[i]
    
for node in range(leafNum-1, 0, -1 ):
    left = node*2
    right = 1+node*2
    tree[node] = tree[left]+tree[right]

def sliceSum(treeNode, treeL, treeR, targetL, targetR):

    if treeR < targetL or targetR < treeL :
        return 0
    
    if targetL<=treeL and treeR <= targetR :
        return tree[treeNode]
    
    mid = (treeL+treeR)// 2
    leftSlice = sliceSum(treeNode*2, treeL, mid, targetL, targetR)
    rightSlice = sliceSum(treeNode*2+1, mid+1, treeR, targetL, targetR)
    
    return leftSlice+rightSlice

def change(b,c):
    leaf = leafNum + (b-1) 
    before = tree[leaf]
    after = c
        
    while leaf >= 1:
        tree[leaf]+= after - before
        leaf = leaf//2


for _ in range(M+K):
    a,b,c = map(int, input().split())
    if a==1 :
        change(b,c)
    elif a == 2:
        rst = sliceSum(1,0,leafNum-1, b-1,c-1)
        print(rst)
        
