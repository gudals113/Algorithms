import time
# 최악의 경우 시간 복잡도 비교
# 선택 < 삽입 < 거품
L = [i for i in range(10000, -1, -1)]
N = len(L)

# 삽입
# start = time.time()
# for i in range(1,N):
#         val = L[i]
#         leftVal_idx = i-1

#         while leftVal_idx >=0 and L[leftVal_idx] > val :
#             L[leftVal_idx+1] = L[leftVal_idx] 
#             leftVal_idx-=1
        
#         L[leftVal_idx+1] = val
        
# end = time.time()
# print(f"{end-start:.5f} sec")

# 선택
# start = time.time()
# for i in range(N):  # 해당 위치 i에 들어갈 원소를 선택
#     minVal_idx = i
#     for j in range(i+1, N):
#         if L[j] < L[minVal_idx]:
#             minVal_idx = j

#     L[i], L[minVal_idx] = L[minVal_idx], L[i]
    
# end = time.time()
# print(f"{end-start:.5f} sec")

# 거품
# start = time.time()
# end = N-1    
# while end>0:
#     lastSwapped=0
#     for i in range(end):
#         if L[i] > L[i+1]:
#             L[i], L[i+1] = L[i+1], L[i]
#             lastSwapped = i    
#     end = lastSwapped
# end = time.time()
# print(f"{end-start:.5f} sec")
