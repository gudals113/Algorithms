#개똥벌레 (누적합)
import sys
input = sys.stdin.readline

N,H = map(int, input().split())
A= [ int(input()) for _ in range(N)] # 전체 저장
prefix=[0 for _ in range(H+1)] #석순 저장
prefix2=[0 for _ in range(H+1)] # 종유석 저장
down = A[::2]   # 석순
up = A[1::2]    # 종유석

down.sort(reverse=True)
up.sort(reverse=True)

idx=down[0] #길이가 큰 석순부터
for i in range(len(down)):
    if down[i]==idx:
        prefix[idx]+=1
    
    else:
        idx=down[i]
        prefix[idx]+=1

#누적합 구하기
for i in range(H-1,0,-1):
    prefix[i]+=prefix[i+1]


idx=up[0] #길이가 큰 종유석부터
for i in range(len(up)):
    if up[i]==idx:
        prefix2[idx]+=1
        
    else:   #길이가 다른 종유석 등장하면 길이(인덱스) 갱신
        idx=up[i]
        prefix2[idx]+=1
        
#누적합 구하기
for i in range(H-1, 0,-1):
    prefix2[i]+=prefix2[i+1]
    


for i in range(1, H+1):
    prefix[i] += prefix2[H+1-i]
sol=prefix[1:]
tmp = min(sol)
print(tmp,sol.count(tmp))