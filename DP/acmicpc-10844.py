#백준 10844번 쉬운 계단수(dp)

row=[ [1] for _ in range(10)  ]
row[0] = [0]
# row[0].append(1)

N=int(input())

for i in range(1, N) :
    for j in range(10):
        if j ==0 :
            row[j].append(row[1][i-1])

        elif j ==9 :
            row[j].append(row[8][i-1])

        else : 
            sumOftwo = row[j-1][i-1] + row[j+1][i-1]
            row[j].append(sumOftwo)

answer=0
for k in range(0, 10) :
    answer+= row[k][N-1]

print(answer%1000000000)