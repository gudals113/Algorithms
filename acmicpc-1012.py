# 백준 1012번 유기농 배추(dfs)
#   그래프 이용해서 풀이 // 2차원 리스트로만 풀이


#DFS 돌리는 로직
def DFS(x, y):

    
    if x<0 or y<0 or x>=w or y>=h:
            return False
    
    dx = [1,-1,0,0]
    dy = [0, 0,1,-1]
    if visited[x][y] == 1:
        visited[x][y]=0
        for i in range(4):
            target_x = x+dx[i]
            target_y = y+dy[i]
            DFS(target_x, target_y)

        return True
    
    return False
        
    
for _ in range(int(input())):
    #큰 격자판 만들기
    
    w,h,K = map(int, input().split()) 
    visited = [[0 for _ in range(h)] for _ in range(w)]

    #배추 있는 곳 표시하기
    for i in range(K):
        x, y = map(int, input().split())
        visited[x][y]=1
    
    #DFS 돌리기
    count=0
    for x in range(w) :
        for y in range(h):
            if DFS(x,y) == True:
                count+=1

    print(count)

