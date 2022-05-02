N,K = map(int,input().split())
L = list(map(int,input().split()))

check = [ [ ]for _ in range(100001) ]

sol = 0
tmp = 0
for i in range(N):
    num = L[i]
    
    if len(check[num]) < K :
        check[num].append(i)  
        tmp+=1
        sol = max(sol, tmp)
 
    else: 
        idx = check[num].pop(0)
        check[num].append(i)
        
        sol = max(sol, tmp)
        tmp = i - idx

sol = max(sol, tmp)
print(sol)

# check[5]=[3,4]
# check[5]=[4,6]

# 11 2
# 3 2 5 5 6 4 4 5 7 2 2

l = f'{}'