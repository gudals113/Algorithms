def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])

    dp = [ [0 for _ in range(M+1)] for _ in range(N+1)]
    
    for type,r1,c1,r2,c2,degree in skill:
        if type == 1:
            degree*=-1

        dp[r1][c1]+=degree
        dp[r1][c2+1]-=degree
        dp[r2+1][c1]-=degree
        dp[r2+1][c2+1]+=degree
    
    newDP = [ [0 for _ in range(M)] for _ in range(N) ]
    
    for x in range(N+1):
        tmp = 0
        for y in range(M+1):
            tmp+=dp[x][y]
            dp[x][y] = tmp


    for y in range(M+1):
        tmp = 0
        for x in range(N+1):
            tmp+=dp[x][y]
            dp[x][y]=tmp
    

    
    for x in range(N):
        for y in range(M):
            board[x][y]+=dp[x][y]
            if board[x][y]>0:
                answer+=1
    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])