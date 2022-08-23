# 최솟값 찾기
# wrong 220801
# 덱으로 푸는 문제


#세그먼트 트리 시간 초과
# import math

# N, M = map(int, input().split())
# L = list(map(int, input().split()))
# node = math.ceil(math.log2(N))
# node = 2**node # leaf node 개수

# INF = float('inf')
# tree = [ INF for _ in range(node*2)]

# #leaf 초기화
# for i in range(N):
#     tree[node+i] = L[i]
    
# for i in range(node-1, 0, -1):
#     left, right  = tree[i*2], tree[(i*2)+1]
    
#     tree[ i ] = min(left, right)

# def DFS(nodeNum, nodeL, nodeR, findL, findR):
#     if nodeR < findL or nodeL > findR :
#         return INF
    
#     if nodeR <=findR  and  findL <= nodeL :
#         if findL==0 and findR==2:
#             print(nodeNum, tree[nodeNum],nodeL, nodeR)
        
#         return tree[nodeNum]

#     mid = (nodeL+nodeR)//2
    
#     leftMin = DFS(nodeNum*2, nodeL, mid ,findL,findR)
#     rightMin = DFS((nodeNum*2)+1, mid+1, nodeR, findL, findR)
#     val = min(leftMin, rightMin)
#     return val

# D = [ 0 for _ in range(N)]
# for i in range(N):
#     s, e = i-M+1 ,i

#     minVal = INF
#     if s>=0 :
#         minVal = DFS(1,0,node-1, s, e )
#     elif s<0:
#         minVal = DFS(1,0,node-1, 0, e)
        
#     D[i]= minVal
# print(*D)

#heap 시간 초과

