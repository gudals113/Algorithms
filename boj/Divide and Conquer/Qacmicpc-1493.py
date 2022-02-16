# import sys 
# sys.setrecursionlimit(5000)
# 박스 채우기 파이썬으로는 재귀 못푸나?
# 통과 못함
box=[]
l,w,h = map(int, input().split())
N = int(input())
for i in range(N):
    box.append(list( map(int, input().split()) ))
    
sol = 0
def dividing(x,y,z) :
    global sol    

    if x==0 or y==0 or z==0 :
        return 0
    
    for idx in range(N-1,-1,-1):
        num = box[idx][1]
        line = 2**box[idx][0]
            
        if num >0 and line<=min(x,y,z):
            box[idx][1] -= 1
            sol+=1
            
            tmp1 = dividing(line,y-line ,line)
            tmp2 = dividing(line,y,z-line)
            tmp3 = dividing(x-line, y,z)
            
            break
        
        if idx==0 and num==0:
            return -1
        
    if tmp1==-1 or tmp2==-1 or tmp3==-1:
        return -1
    
    return sol    
        
tmp = dividing(l,w,h)
print(tmp)