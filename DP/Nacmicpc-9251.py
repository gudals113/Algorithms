#LCS

strA = ' ' + input()
strB = ' ' + input()
lenA = len(strA)
lenB = len(strB)
dp= [[0for _ in range(lenB)]for _ in range(lenA) ]

for i in range(1,lenA):
    wordA=strA[i]
    
    for j in range(1, lenB):
        wordB =strB[j]
        
        if wordA==wordB:
            dp[i][j] = dp[i-1][j-1]+1
        
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[lenA-1][lenB-1])