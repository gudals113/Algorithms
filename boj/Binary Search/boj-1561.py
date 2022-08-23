# boj-1561.py
# 놀이공원
# 220721 sol
# 이분 탐색
N,M = map(int, input().split())
L = list(map(int, input().split()))
s,e = -1, 60000000001

check = 0
while e-s>1:
    
    mid = (s+e)//2
    #mid 시간에 각각 놀이기구에 탑승한 사람 수
    ppl = 0
    for i in range(M):
        time = L[i]
        ppl += ( mid // time ) + 1
    #실제 인원보다 많이 탑승하거나 똑같이 탑승한 사람 수 들 중 최소(low bound)
    if ppl >= N :
        check= mid
        e = mid

    elif ppl < N:
        s = mid
        
candidate = [0]
before ,after =0,0
for i in range(M):
    time = L[i]
    before_ppl =  ((check-1) // time) +1
    after_ppl = ( check // time ) +1
    
    before+= before_ppl
    if before_ppl != after_ppl :
        candidate.append(i)
        
change = N-before
answer = candidate[change]
print(answer+1)