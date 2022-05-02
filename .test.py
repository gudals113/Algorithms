# # #평범한 배낭2
# # N, M = map(int, input().split())
# # stuff = [[0,0,0]]
# # # costSum = 0
# # for _ in range(N) :
# #     line = list(map(int, input().split()))
# #     # costSum += line[0] * line[2]
# #     stuff.append(line)
    
# # # stuff[]  = 무게, 만족도, 개수
# # dp=[ [0 for _ in range(M+1)] for _ in range(N+1) ]

# # # 모든 물품에 대하여 루프
# # for i in range(1, N+1):
# #     cost = stuff[i][0]
# #     bnf = stuff[i][1]
# #     num = stuff[i][2]
# #     idx = num
    
# #     #최대무게 부터 무게1까지 에 대하여 루프 
# #     for j in range(M,0,-1) :
        
# #         dp[i][j] = dp[i-1][j]
        
# #         if j>=cost*idx:
# #             # 여기서 모든 인덱스 봐야겠다? 
# #             dp[i][j] = max(dp[i][j], dp[i-1][j-cost*idx]+bnf*idx)

            
# #         elif 0<=j<cost*idx and idx>1:
# #             idx-=1
# #             if j>=cost*idx:
# #                 dp[i][j] = max(dp[i][j], dp[i-1][j-cost*idx]+bnf*idx)  
# #         print(i,j,dp[i][j])       
    
# # print(dp[N][M])


# # s = '012345'

# # print(s[1:])

# # print(s[:3])
# # print(s[1:3])#차이 크기만큼 리턴
# # print(s[3:1:-1])
# # s =list(s)
# # s.pop()
# # print(s)

# # for i in range(5,-1,-1):
# #     print(i)

# # print('hi')
# # for i in range(1,1):

# for i in range(0):
#     print(i)
    
    
# #비숍 백트래킹
N = int(input())
G=[ ]
visited = [ [-1 for _ in range(N)] for _ in range(N) ]
for _ in range(N):
    G.append(list(map(int, input().split())))

def check(x,y):
    global visited
    for i in range(1,x+1):
        if y-i<0:
            break
        
        if visited[x-i][y-i]==1:
            return False
    
    for i in range(1,x+1):
        if y+i>=N:
            break
        if visited[x-i][y+i]==1:
            return False
        
    return True

def odd_DFS(idx,count):
    global odd_sol
    global visited
    
    if idx >=N**2:
        return count
    
    x=idx//N 
    y=idx%N 
    
    tmp = odd_DFS(idx+2, count) ##################################이게 왜 에러 나는건지 찾아보자!!
    odd_sol = max(odd_sol, tmp)
    odd_sol = max(odd_sol, odd_DFS(idx+2, count)) # 이렇게 하면 왜 안되는거징
    if G[x][y]==1:
        if check(x,y)==True:
            
            visited[x][y] = 1
            
            tmp = odd_DFS(idx+2, count+1)            
            odd_sol = max(odd_sol, odd_DFS(idx+2, count+1) ) 
            
            visited[x][y] = -1
    return count
            
sol=0

if N%2==1:
    odd_sol = 0
    odd_DFS(0,0)
    sol+=odd_sol

    odd_sol=0
    odd_DFS(1,0)
    sol+=odd_sol

    
print(sol)
