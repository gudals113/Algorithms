# Z 분할 정복 sol220527
N, r, c = map(int,input().split())

# visited = -1
# G = [ [0 for _ in range( 2**(N-1) )] for _ in range( 2**(N-1) )]
# def count(N,x,y) :
#     global visited
    
#     if N == 0 :
        
#         visited+=1
#         G[x][y]= visited
#         return
    
    
#     l = 2**(N-1)
#     count(N-1, x,y)
#     count(N-1, x,y+l)
#     count(N-1, x+l,y)
#     count(N-1, x+l,y+l)

# count(N,0,0)

G=[ [0,1],[2,3] ]

def count(N,x,y):
    
    if N == 0:
        return G[x][y]        
    
    l = 2**(N-1)

    if x>=l :
        if y>=l:
            #4번
            sol = count(N-1,x-l,y-l) + (l**2)*3
            return sol
        else:
            #3번
            sol = count(N-1,x-l,y) + (l**2)* 2
            return sol
    else:
        if y >=l :
            #2번
            sol = count(N-1, x,y-l) + (l**2)
            return sol
        else:
            #1번
            sol = count(N-1,x , y)
            return sol
        
answer = count(N, r,c)
print(answer)