from collections import deque


T= int(input())
for _ in range(T):
    N, M = map(int,input().split())
    
    dict={}
    for i in range(1,10):
        dict[i]=0
    
    arr = list(map(int, input().split()))
    for i in range(N):
        dict[arr[i]]+=1
    
    q=deque(arr)
    
    idx,count=M,0 #  M번째 수 현재 위치/출력된 수
    while q:
        
        a = q.popleft()
        
        check=0
        for i in range(a+1,10):
            if dict[i]>0:
                check=1
                break
        
        
        if idx==0:
            if check==0:
                count+=1
                break
            
            elif check==1:
                q.append(a)
                idx=len(q)-1
                continue
        
        if check==0: # 프린트 해야되는 경우
            dict[a]-=1            
            count+=1
            idx-=1
            
        elif check==1: # 프린트 안하고 맨뒤로 넣는 경우
            q.append(a)
            idx-=1
            #count 그대로
    
    print(count)