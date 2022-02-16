#백준 11057번 오르막수 (dp)

# def func1(N, E) :
#     if N==1 :
#         return 1 

#     ans=0
#     for i in range(E,10):
#         ans += func1(N-1, i)
#     return ans

# answer=0
# for i in range(10):
#     answer += func1(N,i)

# print(answer%100007)

N=int(input())
row=[ 1 for _ in range(10)  ]
for i in range(1, N):
    
    for j in range(8,-1,-1):
        row[j] += row[j+1]

answer=0
for i in range(10):
    answer+=row[i]

print(row)
print(answer%10007)