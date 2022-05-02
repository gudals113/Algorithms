#카드 정리하기 우선순위 큐
from heapq import heappop, heappush
N=int(input())
heap=[]
for _ in range(N):
    heappush(heap, int(input()))


sol=0
while len(heap)>1:
    
    a,b = heappop(heap), heappop(heap)
    tmp=a+b
    sol+=tmp
    heappush(heap, tmp)
   
print(sol)
