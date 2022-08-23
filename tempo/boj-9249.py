#최장 공통 부분 문자열
# try 220802
#데이터 크기 때문에 아래와 같은 방식으로 못한다
#알고리즘 테크닉 필요
A = ' '+input()
B = ' '+input()
dp = [[0 for _ in range(len(B))] for _ in range(len(A)) ]
answer = 0
for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i]==B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            
            answer = max(answer, (dp[i][j]))
print(answer)