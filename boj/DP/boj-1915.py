# 가장 큰 정사각형
# hint 220831
# 게시판 질문 참고함
# dp
# 현재 코드 매우 비효율적임(속이 꽉 차지 않은 정사각형 구하려다 보니, 한 칸에 연속되는 길이 저장함)
N, M = map(int, input().split())
G = [[0 for _ in range(M)]for _ in range(N)]
dp = [[0 for _ in range(M)]for _ in range(N)]
for i in range(N):
    l = input()
    for j in range(M):
        
        if l[j]=='1':
            if j == 0 :
                G[i][j] = 1 
            else:
                G[i][j] = G[i][j-1]+1
            
            dp[i][j]=1
            
rotatedG = [[0 for _ in range(M)] for _ in range(N)]
for j in range(M):
    for i in range(0,N):
        
        if G[i][j] > 0 :
            if i == 0 :
                rotatedG[i][j] = 1
            else:
                rotatedG[i][j] = rotatedG[i-1][j]+1

for i in range(1,N):
    for j in range(1,M):        
        w = G[i][j]
        h = rotatedG[i][j]
        before = dp[i-1][j-1]
        if min(w,h) > before :
            dp[i][j] = before + 1
        elif min(w,h) <= before :
            dp[i][j] = min(w,h)
answer=0
for i in range(N):
    for j in range(M):
        answer = max(dp[i][j]**2, answer)

print(answer)

