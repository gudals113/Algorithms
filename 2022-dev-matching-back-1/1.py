
#최단 거리 , 
def solution(dist):
    answer = []
    N= len(dist)
    
    zp=0
    maxDist=0
    for i in range(N): #0 점에 완탐
        tmp = max(dist[i])
        if tmp > maxDist :
            maxDist = tmp
            zp = i
    
    E = dist[zp]
    dict={}
    
    for i in range(N):
        dict[E[i]] = i
    sdict = sorted(dict.items())
    sol =[]
    for i in range(N):
        sol.append(sdict[i][1])
        
    answer.append(sol)
    answer.append(sol[::-1])
    answer.sort()
    # print(answer)
    return answer


solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]])