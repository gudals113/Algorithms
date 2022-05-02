#개똥벌레
N,H = map(int,input().split())

bottom = []
top=[]

for i in range(N):
    num = int(input())
    if i %2==0:
        bottom.append(num)
    else:
        top.append(num)
        
prefix_bottom =[0 for _ in range(H+1)] 
prefix_top=[0 for _ in range(H+1)]

for num in bottom:    
    # num = bottom[i]
    prefix_bottom[num]+=1

for i in range(H-1,0,-1):
    prefix_bottom[i] +=prefix_bottom[i+1]


for num in top:
    prefix_top[num]+=1
        
for i in range(H-1,0,-1):
    prefix_top[i] +=prefix_top[i+1]


for i in range(1, H+1):
    prefix_bottom[i] += prefix_top[H-i+1]
    
tmp = min(prefix_bottom[1:])
count=0
for i in range(1, H+1):
    if prefix_bottom[i]==tmp:
        count+=1
# print(prefix_bottom)
# print(prefix_top)
print(tmp, count)
