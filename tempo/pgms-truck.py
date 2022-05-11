#다리를 지나는 트럭
#https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    N=len(truck_weights)
    
    truck_weights.sort(key=lambda x:(-x[0]))
        
    q = deque([])
    time = 0
    tmp = weight
    for i in range(N):
        if tmp- truck_weights[i] >=0 and truck_weights[i]!=-1:
            tmp+=truck_weights[i]
            truck_weights=-1 #방문표시
            q.append(i)

    
    return answer