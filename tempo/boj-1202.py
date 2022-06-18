#보석 도독 greedy, priority queue, sol220526
from heapq import heappop, heappush
N, K = map(int,input().split())

jew_list = []
for _ in range(N):
    M, V = map(int, input().split())
    jew_list.append([M,V])

bag_list = []
for _ in range(K):
    C = int(input())
    bag_list.append(C)
    
bag_list.sort()
jew_list.sort()

jew_idx=0
answer = 0
heap=[]

for i in range(K):
    c = bag_list[i]
    
    
    
    while jew_idx<N:
        
        m,v = jew_list[jew_idx]
        
        if m<=c:
            heappush(heap, -1*v )
            jew_idx+=1
            
        elif m > c :
            break
    
    
    
    if heap :
        tmp = heappop(heap)
        answer += -1 * tmp

    
print(answer)

