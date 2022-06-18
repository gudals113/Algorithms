#팰린드롬? DP, 220607 sol
import sys
input = sys.stdin.readline
N = int(input())
board = list(map(int,input().split()))
M = int(input())
Q = [[0 for _ in range(N)]for _ in range(N)]

for i in range(N):
    Q[i][i]=1
    
for length in range(2,N+1):
    for start in range(N-length):
        end = start + length -1
        
        if board[start]==board[end] :
            if length==2:
                Q[start][end]=1
            
            elif Q[start+1][end-1]==1:
                Q[start][end]=1      
        else:
            Q[start][end]=-1
    
        
for i in range(M):
    a,b = map(int,input().split())
    if Q[a-1][b-1]==1:
        print(1)
    else:
        print(0)

