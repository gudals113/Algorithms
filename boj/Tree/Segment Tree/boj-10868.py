#최솟값
# hint 220802 10:05 - 
# segment tree

# 진짜, 무조건 큐 같은데 , 창의적 테크닉이 필요할듯 
# 아니네, 그냥 세그먼트 트리네. 딱봐도..

import math
INF = float('inf')

N,M = map(int, input().split())
L,Q  = [] , []
for _ in range(N):
    L.append(int(input()))
for i in range(M):
    a,b = map(int, input().split())
    Q.append([a,b])

leafNum = math.ceil(math.log2(N))
leafNum = 2**leafNum
treeNum = leafNum*2
#root:1번, leaf : L_idx + leafNum번
tree = [ INF for _ in range(treeNum)]


#리프 레벨 갱신
for i in range(N):
    tree[i+leafNum] = L[i]
    
#리프 위 레벨 부터, 루트 레벨까지 갱신
for i in range(leafNum-1, 0, -1):
    left,right = tree[i*2], tree[i*2+1]
    tree[i] = min(left, right)
        
def find(treeL,treeR,nodeNum,findL,findR):
    if findR<treeL or treeR<findL:
        return INF
    
    if findL<=treeL and treeR<=findR:
        return tree[nodeNum]
    
    mid = (treeL+treeR)//2
    
    left = find(treeL,mid, nodeNum*2, findL, findR)
    right = find(mid+1,treeR, nodeNum*2+1, findL, findR)
    return min(left,right)


### 항상 여기서 틀렸다. N이 아니라. leafNum을 기준으로 찾아야한다.
for a,b in Q:
    sol = find(0,leafNum-1,1,a-1,b-1)
    print(sol)