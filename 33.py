# 33.py
d =  {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6 }
dp=[0 for _ in range(100)]
for i in range(10):
    dp[d[i]]+=1


for i in range(51):
    for j in range(2,10):
        dp[i+j] += dp[i]

# print(dp[11])