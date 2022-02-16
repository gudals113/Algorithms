#백준 16434번 드래곤 앤 던전 (binary search)
#ing

N, A = map(int, input().split())

room = []
for _ in range(N):
    arr = list(map(int, input().split()))
    room.append(arr)

s = 0
t = int(1e18)
sol=0

while t-s > 1:
    
    m = (s+t)//2
    currentHP = m
    currentA = A

    # print(s,t,m)

    for i in range(N):
        nowhere = room[i]

        if nowhere[0] == 1:
            if  nowhere[2] % currentA  == 0:
                currentHP -= ((nowhere[2]//currentA)-1) * nowhere[1]
         
            else:
                currentHP -= (nowhere[2]//currentA) * nowhere[1]
            
            if currentHP<=0 :
                break

        elif nowhere[0] == 2:
            currentA += nowhere[1]
            currentHP = min(m, currentHP+nowhere[2])

        

    if currentHP  > 0:
        t = m
        sol = m
    else:
        s = m

print(sol)
