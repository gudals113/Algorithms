from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

def solution(k, room_number):
    room = defaultdict(int)
    answer = []

    def find(u):
        if u not in room :
            room[u] = u+1
            return u
        
        room[u] = find(room[u])
        return room[u]
        
        
    for i in range(len(room_number)):
        want = room_number[i]
        target = find(want)
        answer.append(target)
   
    return answer



#union-find 기본 구조로 풀기 실패
# def solution(k, room_number):
#     answer = []
#     def find(u):
#         if p[u] ==-1:
            
#             return u
        
#         p[u] = find(p[u])
#         return p[u]
    
#     #v가 부모
#     def union(u,v):
#         u = find(u)
#         v = find(v)
#         if u==v:
#             return True
        
#         p[v] = u
                
#     p = [-1 for _ in range(k+2)]

#     for i in range(len(room_number)):
#         want = room_number[i]
#         target = find(want)    
#         answer.append(target)
#         union(target+1, target)
#     return answer

# rst = solution(10,[1,3,4,1,3,1])
# print(rst)


#union-find 고치고 find만 사용
# def solution(k, room_number):
#     answer = []
#     def find(u):
#         if p[u] ==-1:
#             p[u]= u+1
#             return u
        
#         p[u] = find(p[u])
#         return p[u]
    
                
#     p = [-1 for _ in range(k+2)]

#     for i in range(len(room_number)):
#         want = room_number[i]
#         target = find(want)    
#         answer.append(target)
#     return answer

# rst = solution(10,[1,3,4,1,3,1])
# print(rst)