N=int(input())
arr=list(map(int, input().split()))
dp=[ 0 for _ in range(N)  ]

for i in range(N):
    if dp[i]==0 :
        for j in range(i, N-i):
            check = 0
            if arr[j] > check:
                check = arr[j]
                dp[i] += check

print(arr)
print(dp)

