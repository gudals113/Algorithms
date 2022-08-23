# boj-8983.py
#사냥꾼
#이분 탐색
#sol220718
M, N, L = map(int, input().split())
hunter = list( map(int, input().split()))
target = []
for _ in range(N):
    target.append(list(map(int, input().split())))

hunter.sort()
answer={}
for i in range(N):
    x,y = target[i]
    ta,tb = x-y, x+y
    
    s,e =-1, len(hunter)

    while e-s>1:
        mid = (s+e)//2
        
        h = hunter[mid]
        ha, hb = h-L, h+L
        
        if h >= x :
            e=mid
            
            if h-L<=ta<=h+L:
                answer[i]=1
                break
    
        elif h<x :
            s=mid
            if h-L <=tb <= h+L:
                answer[i]=1
                break
            
print(len(answer))
        
            
    
    
    

