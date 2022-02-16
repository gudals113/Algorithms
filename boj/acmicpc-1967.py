# #트리의 지름 (미제출)
N = int(input())
tree = [ [] for _ in range(N+1) ]
for _ in range(N-1):
    parent, child, cost = map(int,input().split())
    tree[parent].append([child,cost])
