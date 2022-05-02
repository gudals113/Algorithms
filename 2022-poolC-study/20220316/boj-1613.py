import sys
input = sys.stdin.readline

def find(u, v): #u의 부모를 찾을 때 v가 나타나는지 체크
    if p[u] == v:
        return True
    
    if p[u]==u:
        return False

    
    
    p[u]=find(p[u], v)
    

N,K = map(int,input().split())
p=[i for i in range(N+1)]
for _ in range(K):
    a,b = map(int,input().split())
    # p[b]=a
    
S= int(input())
for _ in range(S):
    
    