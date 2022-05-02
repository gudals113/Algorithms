# #배 greedy
# N = int(input())
# C= list(map(int, input().split()))

# M = int(input())
# B = list(map(int, input().split()))

# C.sort(key=lambda x:-x)
# B.sort(key=lambda x:-x)

# sol=0
# count=0
# visited=[0 for _ in range(M)]
# if B[0] > C[0]:
#     print(-1)
# else:
#     while count<M:

#         for crain in range(N):              
            
#             for box in range(len(B)): 
                        
#                 if not visited[box] and B[box] <= C[crain] :
                    
#                     count+=1
#                     visited[box]=1
                    
#                     break
#         sol+=1
        
#     print(sol)

       
 
N = int(input())
C = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

C.sort(key=lambda x:-x)
B.sort(key=lambda x:-x)

sol = 0 # 시간
visited = [0 for _ in range(M)] # 박스를 옮겼는지 여부
count = 0 # 옮긴 박스의 개수 

positions = [0] * N

if B[0] > C[0]:
    print(-1)
else:
    while count < len(B):
        for i in range(N): # 크레인에 대하여
            while positions[i] < len(B):
            # 아직 안 옮긴 박스 중에서, 옮길 수 있는 박스를 만날 때까지 반복
                if not visited[positions[i]] and C[i] >= B[positions[i]]:
                    visited[positions[i]] = 1
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
        sol += 1
        # print(positions)
    print(sol)