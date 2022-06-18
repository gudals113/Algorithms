from collections import defaultdict


N, d, k , c = map(int,input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))
sushi.extend(sushi)

eaten = defaultdict(int)
eaten[c]=1

for i in range(k):
    eat = sushi[i]
    eaten[eat] += 1

tmp = len(eaten)

for i in range(N):
    spit = sushi[i]
    eat = sushi[i+k]
    
    eaten[eat]+=1
    eaten[spit]-=1
    
    if eaten[spit] == 0:
        del eaten[spit]

    tmp = max(tmp,len(eaten))

print(tmp)
