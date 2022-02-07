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
        
        tmp.append(arr[i])
        nDFS(i+1)
        tmp.pop()


nDFS(0)

for i in range(len(ans)):
    print(ans[i])

# i=1
# while True:
#     if i == len(ans):
#         break
#     if ans[i] == ans[i-1]:
#         ans.pop(i)
#     else:
#         i+=1

# for i in range(len(ans)):
#     print(' '.join(map( str, ans[i])))
    
    
            
