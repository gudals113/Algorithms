N, M = map(int, input().split())
arr = list( map(int, input().split()))
arr.sort()
ans =[]
tmp=[]
dic={}
def nDFS(idx):    
    
    if len(tmp)==M:
        
        stred = (' '.join(map( str, tmp)))
        if stred not in dic:
            dic[stred]=1
            ans.append(stred)
        return
    
    if idx ==N+1:
        return
    
    for i in range(N):
        if tmp==[] or arr[i]>=tmp[-1] :
            tmp.append(arr[i])
            nDFS(i+1)
            tmp.pop()


nDFS(0)

for i in range(len(ans)):
    print(ans[i])