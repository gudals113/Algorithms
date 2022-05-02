# #레드 블루 스패닝 트리
# # 시간 초과 ㅋㅋ
# import itertools
# def find(u) :
#     if p[u]<0:
#         return u
#     p[u] = find(p[u])
#     return p[u]

# def union(u,v) : #v가 루트가 된다.
#     u,v = find(u),find(v)
#     if u==v:
#         return
#     if u < v:
#         p[v]=u
#     else:
#         p[u]=v
        
# maxCost = float('inf')     
# while True:
#     N,M,k = map(int, input().split())
#     if [N,M,k] == [0,0,0] :
#         quit()
#     G=[]
#     Blue=[]
#     Red=[] 
#     for _ in range(M):
#         c,f,t = input().split()
#         f,t = int(f),int(t)
#         if c=='R':
#             Red.append([maxCost,f,t])
            
#         else:
#             Blue.append([1,f,t])

#     combination = itertools.combinations(Blue,k)
#     ans=0
#     for comb in combination:
#         p=[-1 for _ in range(N+1)]
#         G= list(comb) + Red
#         G.append([0,0,0])
#         sol=0
#         count=0
#         isMST=False
        
#         for i in range(len(G)):
#             if count==N-1:
#                 isMST=True
#                 break
#             cost,u,v = G[i]
            
#             if find(u)!=find(v):
#                 if cost==1:
#                     sol+=cost
#                 count+=1
#                 union(u,v)
#         if isMST==True and sol==k:
#             ans=1
#             break
        
#     print(ans)
    
#레드 블루 스패닝 트리
# 시간 초과 ㅋㅋ
import itertools
def find(u) :
    if p[u]<0:
        return u
    p[u] = find(p[u])
    return p[u]

def union(u,v) : #v가 루트가 된다.
    u,v = find(u),find(v)
    if u==v:
        return
    if u < v:
        p[v]=u
    else:
        p[u]=v
        
maxCost = float('inf')     
while True:
    N,M,k = map(int, input().split())
    if [N,M,k] == [0,0,0] :
        quit()
    G=[]
    Blue=[]
    Red=[] 
    for _ in range(M):
        c,f,t = input().split()
        f,t = int(f),int(t)
        if c=='R':
            Red.append(['R',f,t])
            
        else:
            Blue.append(['B',f,t])


    p=[-1 for _ in range(N+1)]
    
    G.append([0,0,0])
    sol=0
    count=0
    isMST=False
    
    for i in range(len(G)):
        if count==N-1:
            isMST=True
            break
        cost,u,v = G[i]
        
        if find(u)!=find(v):
            if cost==1:
                sol+=cost
            count+=1
            union(u,v)
            
    if isMST==True and sol==k:
        print(1)
        
    else:
        print(0)
        
