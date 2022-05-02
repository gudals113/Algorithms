#이중 우선순위 큐
from heapq import heappop, heappush
T=int(input())
for _ in range(T):
    length = 0 
    k=int(input())
    idx=0
    dict={}
    for _ in range(k):
        INS, n = input().split()
        if length==0:
            minHeap=[]
            maxHeap=[]
            
        if INS=='I':
            length+=1
            # dict[idx]=1
            heappush(minHeap, [int(n),idx])
            heappush(maxHeap, [-int(n),idx])
            idx+=1
            
        elif length>0:
            length-=1
            if n=='-1' :
                while True:
                    val, i = heappop(minHeap)
                    if i not in dict:
                        dict[i]=1
                        break
                
            elif n=='1' :
                while True:
                    val, i = heappop(maxHeap)                                
                    if i not in dict:
                        dict[i]=1
                        break
                    
    if length==0:
        print('EMPTY')

    else:
        while True:
            maxVal, i = heappop(maxHeap)
            if i not in dict:
                break
        while True:
            minVal, i = heappop(minHeap)
            if i not in dict:
                break    
        print(-maxVal ,minVal)
