N=int(input())
O=[0]+list(map(int, input().split()))
E=[0]+list(map(int, input().split()))
MO=[[0 for _ in range(N+1)] for _ in range(N+1)]
ME=[[0 for _ in range(N+1)] for _ in range(N+1)]

print(O)
print(E)

# initialize
for i in range(N+1):
    
    MO[1][i]=O[1]
    MO[i][0]=O[i]
    
for i in range(1,N+1):
    if (O[1]>E[i]) or (O[1]+E[i]<0) :
        ME[1][i]=0
    else:
        ME[1][i]=O[1]+E[i]



#main loop
for i in range(2,N+1):
    for j in range(1, N+1):

        tmp=O[i]
        for k in range(1, j+1):
            if O[i]>=E[k]:
                tmp = max(ME[i-1][k] + O[i] , tmp) 


        MO[i][j]= tmp

        
        tmp=0
        for k in range(1, i+1) :
            if E[j]>=O[k] :
                tmp = max(MO[k][j-1]+ E[j] , tmp) 
               

        ME[i][j]= tmp

print('hello')
print(MO)
print(ME)
# print(max(MO), max(ME))

# print(max(ME), max(MO))



