#이중 우선순위큐 (heapq)
from heapq import heappop, heappush

def solution():
    k = int(input())
    id = [False for _ in range(1000001)]
    maxHeap = []
    minHeap = []
    
    for i in range(k):
        inst, num = input().split()
        if inst =='I' :
            id[i]=True
            heappush(maxHeap, (-int(num), i) )
            heappush(minHeap, (int(num),i))
        
        elif num=='1':
            
            while maxHeap and id[maxHeap[0][1]] == False:
                VAL,ID = heappop(maxHeap)
            
            if maxHeap:
                VAL,ID = heappop(maxHeap)
                id[ID]=False
                
                
        else: 
            
            while minHeap and id[minHeap[0][1]] == False:
                VAL,ID = heappop(minHeap)
            
            if minHeap:
                VAL,ID = heappop(minHeap)
                id[ID]=False
                
    while minHeap and id[minHeap[0][1]] == False:
        VAL,ID = heappop(minHeap)
        
    while maxHeap and id[maxHeap[0][1]] == False:
        VAL,ID = heappop(maxHeap)
        
    if maxHeap :
        max_sol, min_sol = maxHeap[0][0], minHeap[0][0]
        print(max_sol*-1, min_sol)
    else:
        print('EMPTY')
        

T= int(input())
for _ in range(T):
    solution()