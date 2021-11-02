#백준 11054번 (DP)
N=int(input())
arr = list( map(int, input().split()) )

incs = [1 for _ in range(N)]
decs = [1 for _ in range(N)]

if N>1:
    for i in range(N):

        tmp=0
        
        for j in range(i):
            if arr[j]<arr[i]:
                tmp = max(tmp,incs[j])  

        incs[i] = tmp+1

    for i in range(N-1,-1,-1):
        
        tmp=0
        for j in range(N-1, i, -1):
            if arr[i]>arr[j]:
                tmp = max(tmp, decs[j])
        decs[i]= tmp+1

    sol=0
    # print(incs, decs)
    for i in range(N):
    
        sol=max(sol,incs[i] + decs[i] -1) 
    
    print(sol)
else:
    print(1)