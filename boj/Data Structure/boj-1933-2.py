# 220718 - 220810 sol
# 스카이라인
# 우선순위 큐 

from heapq import heappop, heappush
N = int(input())
height = [0 for _ in range(N)]
plane = []
whenEnd = [0 for _ in range(N)]


for i in range(N):
    l,h,r = map(int, input().split())
    plane.append([l,i,1]) # start
    plane.append([r,i,0]) #end
    
    height[i] = h
    whenEnd[i]= r

    
plane.sort(key=lambda x: (x[0],x[2])) # 같은 좌표라면 끝나는거 먼저 등장
heap  = []
answer = {}
maxHeight = 0

for i in range(len(plane)): 
    x,idx, isStart = plane[i]
    h = height[idx]
    if isStart:
        if ( heap and -1*heap[0][0] < h ) or not heap:
            if x in answer and maxHeight == h: 
                del answer[x]
                
            elif x not in answer or (x in answer and answer[x] < h ):
                answer[x] = h
        
        maxHeight = max(maxHeight,h)
        
        heappush(heap, [ -1*h, idx ]) 


    elif not isStart :
        while heap :
            pastidx = heap[0][1]
            pastend = whenEnd[pastidx]
            if x < pastend :  
                break
            
            popH, popIDX = heappop(heap)
        
        if heap :
            if -1*heap[0][0] < h :
                answer[x] = -1*heap[0][0]
        else:
            answer[x] = 0
        
                  
sol = []
for key in answer:
    sol.append(key)
    sol.append(answer[key])
print(*sol)