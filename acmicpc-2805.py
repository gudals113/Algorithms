#백준 2805번 나무 자르기 (binary)
N, M = map(int, input().split()) 
arr=list(map(int, input().split()))

low=0
hi = max(arr)

while hi-low>1 :
    total = 0 
    mid = (low + hi ) // 2
    
    for i in range(N):
        wood = arr[i] - mid
        if wood >0 :
            total += wood 
   
    if total >= M :
        low = mid

    else :
        hi = mid
    
print(low)