# 커피숍 2
# 220913
# 세그먼트 트리
from math import ceil, log2

N,Q = map(int, input().split())
L = list( map(int, input().split()) )

leafNum = 2**( ceil(log2(N)) )
nodeNum = 2*leafNum
#tree에 합 저장.
tree= [0 for _ in range(nodeNum)]

for leaf in range(N):
    tree[leaf + leafNum] = L[leaf]

for node in range(leafNum-1,0,-1):
    tree[node] = tree[node*2] + tree[(node*2)+1]

# L에서 node번째 위치 수 변경
def updateTree(node, newVal):
    node = node-1+leafNum
    tree[ node ] = newVal

    parent = node//2

    while parent>=1:
        tree[parent]= tree[parent*2] + tree[(parent*2)+1]
        parent = parent//2

def getSum(targetL, targetR, treeL, treeR, treeNum):
    
    if targetR < treeL or treeR < targetL :
        return 0
    
    if targetL<=treeL and treeR<=targetR :
        return tree[treeNum]
    
    mid = (treeL+treeR)//2
    left = getSum(targetL, targetR, treeL, mid, treeNum*2)
    right = getSum(targetL, targetR, mid+1, treeR, (treeNum*2)+1)
    
    return left+right    
    
for _ in range(Q):
    x,y,a,b = map(int,input().split())
    if x>y :
        x,y = y,x
    rst = getSum(x-1,y-1,0,leafNum-1,1)
    print(rst)
    
    updateTree(a,b)
    