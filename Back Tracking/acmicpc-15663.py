N, M = map(int, input().split())
arr = list( map(int, input().split()))
arr.sort()

check=[0 for _ in range(N)]
ans=[]
tmp=[]

def DFS():
    global tmp,check,ans
    
    if len(tmp)==M:
        ans.append(tmp[:]) 
        
        return

    for i in range(N):
        if check[i] == 0:
            check[i]=1
            tmp.append(arr[i])
            DFS()
            check[i]=0
            tmp.pop()
                   
DFS()
ans.sort()

i=1
while True:
    if i == len(ans):
        break
    if ans[i] == ans[i-1]:
        ans.pop(i)
    else:
        i+=1
    
    # print(ans)
    

for i in range(len(ans)):
    print(' '.join(map( str, ans[i])))
    
