# 최솟값과 최댓값
# 세그먼트 트리
# 220802

import sys
import math
input = sys.stdin.readline
INF = 1_000_000_001

N, M = map(int, input().split())
L = []
for _ in range(N):
    L.append(int(input()))
    
leafNode = math.ceil(math.log2(N))
leafNode = 2**leafNode
treeNode = 2*leafNode

#최솟값, 최댓값 저장
tree = [ [ INF, 0] for _ in range(treeNode) ]
#initialize

for i in range(N):
    tree[i+leafNode][0] = L[i]
    tree[i+leafNode][1] = L[i]

for i in range(leafNode-1,0,-1):
    leftMin,leftMax = tree[i*2]
    rightMin, rightMax = tree[i*2+1]

    tree[i][0] = min(leftMin, rightMin)
    tree[i][1] = max(leftMax, rightMax)
    
def find(treeL, treeR, nodeNum ,findL,findR):
    if findR < treeL or treeR < findL :
        return INF, 0
    
    if findL<=treeL and treeR<=findR :
        return tree[nodeNum][0], tree[nodeNum][1]
        
    mid = ( treeL+treeR )//2
    leftMin, leftMax = find(treeL, mid, nodeNum*2, findL, findR)
    rightMin, rightMax = find(mid+1, treeR, nodeNum*2+1, findL, findR)
    return min(leftMin, rightMin), max(leftMax, rightMax)

for _ in range(M):
    a,b = map(int, input().split())
    solMin, solMax = find(0,leafNode-1, 1, a-1,b-1)
    print(solMin, solMax)