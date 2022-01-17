N=int(input())
k=int(input())
dict={}
for i in range(1, N+1):
    for j in range(1,N+1):
        if i*j in dict:
            dict[i*j]+=1
        else:
            dict[i*j]=1

while True:
    