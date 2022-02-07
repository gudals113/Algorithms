N, M = map(int, input().split())
arr = list( map(int, input().split()))
arr.sort()
ans =[]
tmp=[]
def DFS(idx):
        
    if len(tmp)==M:
        ans.append(tmp[:])
        return
    
    if idx == N:
        return 
    
    if tmp==[] or tmp[-1] <= arr[idx]:
        
        tmp.append(arr[idx])
        DFS(idx+1) 
        tmp.pop()
        
    DFS(idx+1)

def nDFS(idx):    
    
    if len(tmp)==M:
        ans.append(tmp[:])
        return
    
    if idx ==N:
        return
    
    for i in range(idx,N):
        if tmp==[] or tmp[-1] <= arr[i]:
            tmp.append(arr[i])
            nDFS(i+1)
            tmp.pop()

# DFS(0)
nDFS(0)

ans.sort()
i=1
while True:
    if i == len(ans):
        break
    if ans[i] == ans[i-1]:
        ans.pop(i)
    else:
        i+=1

for i in range(len(ans)):
    print(' '.join(map( str, ans[i])))
    
    
            
