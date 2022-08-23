# 1351번 무한 수열
# sol220714, hash
import math

N, P, Q = map(int, input().split())

dp = {}
dp[0]=1

def DFS(idx):
    if idx not in dp:
        
        x = math.floor(idx/P)
        dx = DFS(x)
        
        y = math.floor(idx/Q)
        dy = DFS(y)
        
        dp[idx] = dx+dy
    
    return dp[idx]

answer = DFS(N)
print(answer)