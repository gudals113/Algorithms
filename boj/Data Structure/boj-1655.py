# 가운데를 말해요
# hint-구글링 220808 
# 우선순위 큐
# 2개 써야된다는 거 알았는데 그냥 답지 봤다.

from heapq import heappop, heappush

N = int(input())
leftHeap =[]
rightHeap = []
L = []
for i in range(N):L.append(int(input()))
mid = L[0]
answer=[mid]
for i in range(1,N):
    num = L[i]
    if mid <=num :
        heappush(rightHeap,num)
    else:
        heappush(leftHeap,-1*num)
        
    if (i+1)%2==0 :
        if len(leftHeap) > len(rightHeap) :
            heappush(rightHeap, mid)
            mid = -1*heappop(leftHeap)
            
    else:
        if len(leftHeap)+2==len(rightHeap) :
            heappush(leftHeap, -1*mid)
            mid = heappop(rightHeap)

    answer.append(mid)
    
        
    
for a in answer:
    print(a)
        
    
 