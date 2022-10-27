# 종이 조각
# 220915
# bitmask
N, M = map(int, input().split())
G=[input() for _ in range(N)]
answer = 0
def check(g):
    #가로 조각만 세어보자.

    sumBlock=0
    for i in range(N):
        bitNum = g[i]
        strNum = '0'
        for j in range(M-1,-1,-1):
            if 1<<j & bitNum >= 1:
                sumBlock += int(strNum)
                strNum = '0'
            else:
                strNum += G[i][M-(j+1)]
        sumBlock += int(strNum)
    
    for i in range(M-1,-1,-1):
        
        strNum = '0'
        for j in range(N):
            if 1<<i & g[j] ==0 :
                sumBlock += int(strNum)
                strNum = '0'
            else:
                strNum += G[j][M-(i+1)]
            
        sumBlock+= int(strNum)

    return sumBlock

# M bit 표현 가능
# 0 - 2**M - 1 숫자 고르기. 세로 조각으로 사용될 애들만 표시.
def DFS(row, bitG):
    global answer
    
    if row == N:
        rst = check(bitG)
        answer = max(rst,answer)
        return
    
    for bitNum in range(0,2**M):
        bitG.append(bitNum)
        DFS(row+1, bitG)
        bitG.pop()

DFS(0,[])
print(answer)         