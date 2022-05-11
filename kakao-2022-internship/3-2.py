#시간초과

#셀프 수련을 개선해야할듯
def solution(alp, cop, problems):
    
    global sol, visited
  
    sol = 100

    visited= [0 for _ in range(len(problems))]
    # self=[0,0]
    def check(a, c):
        for i in range(len(problems)) :
            if problems[i][0] > a or problems[i][1] > c :
                return False
        return True
    
    def DFS(time, self_al, self_co) :
        global sol, visited
 
        if time > sol :
            return

        algo, codi = alp+self_al, cop+self_co
        
        for i in range(len(visited)) :
            algo += visited[i] * problems[i][2]
            codi += visited[i] * problems[i][3]

        if check(algo, codi) :
            sol = min(sol, time)
            return

        for i in range(len(problems)+1):
            if i == len(problems) :
                DFS(time+1, self_al+1, self_co)
                DFS(time+1, self_al, self_co+1)
            
            elif problems[i][0] <= algo and problems[i][1] <= codi:
                visited[i] +=1
                DFS(time + problems[i][4], self_al, self_co)
                visited[i] -=1


    DFS(0, 0, 0)
    print(sol)
    return sol

rst = solution(10,	10,	[[10,15,2,1,2],[20,20,3,3,4]])