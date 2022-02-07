from itertools import combinations

N, M = map(int, input().split())
# city = [ [ 0 for _ in range(N) ] for _ in range(N)]

loc_chicken = []
loc_house = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N) :
        w = line[j]
        # city[i][j] = w
        if w ==1:
            loc_house.append([i,j])
        elif w == 2:
            loc_chicken.append([i,j])
                
distance_htoc=[]

#집에서 치킨집까지 모든 거리 구하기 O(2N * 13)
for house in loc_house : 
    x, y = house[0], house[1]
    tmp=[]
    for chicken in loc_chicken : 
        a,b = chicken[0], chicken[1]
        dis = abs(x-a) + abs(y-b)
        
        tmp.append(dis)
        
    distance_htoc.append(tmp)

ans = float('INF')
len_house = len(loc_house)
len_chicken = len(loc_chicken)


comb = list( combinations( [ i for i in range(len_chicken) ], M ) )
# print(comb)
for i in range(len(comb)): 
    toleft = comb[i]  # 총 개수가 op개인 조합들 toleft = (0,1) (1,2) (0,2)
    
    sol=0       
    for j in range(len_house): #집에서 치킨집까지 거리 리스트 모든 집에 대하여 루프
        
        tmp_j=2*N
        for e in (toleft) :  # 조합에서 고를 수 있는 치킨 집 인덱스 e
            tmp_j = min(tmp_j, distance_htoc[j][e])
        sol+=tmp_j
        
        
    ans = min(ans, sol)           



print(ans) 