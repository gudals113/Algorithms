from copy import deepcopy


def checkShaep(G,target,sx,sy):
    l = []
    if sx+2<N and G[sx+2][sy]==target:
        # 길쭉 ㄴ
        if sy+1<N and G[sx+2][sy+1]==target :
            l.append([sx,sy+1])
            l.append([sx+1,sy+1])
            
        # 길쭉 ㄴ 뒤집은 모양    
        elif sy-1>=0 and G[sx+2][sy-1]==target:
            l.append([sx,sy-1])
            l.append([sx+1,sy-1])
    
    #ㅗ 모양
    elif sx+1<N and sy-1>=0 and sy+1<N and G[sx+1][sy-1]==target and G[sx+1][sy+1]==target:
        l.append([sx,sy-1])    
        l.append([sx,sy+1])
    
        
    elif sx+1<N and G[sx+1][sy]==target:
        #누운 ㄴ 모양
        if sy+2<N and G[sx+1][sy+2]==target:
            l.append([sx,sy+1])
            l.append([sx,sy+2])
        
        #누운 ㄴ 모양 뒤집은 형태
        elif sy-2>=0 and G[sx+1][sy-2]==target:
            l.append([sx,sy-1])
            l.append([sx,sy-2])
    
    
    return l

def eraseBlock(G,checkList, target):
    newG = deepcopy(G)
    for x,y in checkList:
        nx = x
        while nx>=0:
            if G[nx][y]==0:
                nx-=1
            
            else:
                return False, []
    
    for x in range(N):
        for y in range(N):
            if newG[x][y]==target:
                newG[x][y]=0
                
    return True, newG            
            
    
def find(G):
    global answer
    again = 1
    while again>0:
        for x in range(N):
            for y in range(N):
                if G[x][y]>0 : 
                    target = G[x][y]
                    sx,sy = x,y
                    checkList = checkShaep(G,target,sx,sy)
                    if len(checkList)==2:
                        rst, newG = eraseBlock(G,checkList,target)
                        if rst:
                            G = newG
                            answer+=1
                            again=2
        again-=1

def solution(board):
    global N, answer
    answer = 0

    N = len(board)
    

    find(board)
    
    return answer


solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])