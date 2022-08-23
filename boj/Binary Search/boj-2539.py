# 모자이크
# 이분 탐색
# 220722 sol
N, M = map(int,input().split())
K = int(input())
F = int(input())
G = []
#도화지의 밑면에 붙이기 때문에 최소 길이는 x좌표 중 최댓값
#최대 길이는 세로와 가로 길이 중 최솟값
minL = 0
maxL = 1_000_000
for _ in range(F):
    x,y = map(int, input().split())    

    #색종이가 붙어있는 y좌표만 저장
    #최소 길이 갱신
    G.append(y)
    minL = max(x, minL)
    
setG = set(G)
G = list(setG)
G.sort()

s,e = minL-1, maxL+1  
answer = 0
while e-s > 1:
    #색종이 길이 = mid
    mid = (s+e)//2
    
    used = 0
    covered = 0
    for i in range(len(G)):
        y = G[i]
        if covered < y :
            covered = y + mid -1
            used+=1 

    if used <= K :
        answer = mid
        e = mid
        
    else :
        s = mid

print(answer)  
    