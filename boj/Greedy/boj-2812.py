#크게 만들기 그리디
N, k = map(int, input().split())
num= list(input())
K=k
sol=[]
for i in range(N):
    while len(sol)!=0 and K>0 and sol[-1] < num[i] :
        sol.pop()
        K-=1
    sol.append(num[i])

print(''.join(sol[:N-k]))




        
    
    



# count=K      #지워야 하는 개수
# start_idx=0  #시작 기준

# def erase(num):
#     global count, start_idx
#     candidate = num[start_idx:start_idx+count+1]
    
    
#     tmp = max(candidate)
#     idx= candidate.index(tmp)
#     print(num, candidate,idx)
    
#     if idx==0:
#         if len(candidate)==1:
#             start_idx=1
#             count-=1
#             return num[:len(num)-1]
        
#         start_idx+=1
#         return num
    
#     else:
#         start_idx=1
#         count-=idx
#         return num[idx:]

# num = A
# while count>0:
#     num = erase(num)

# print(num)