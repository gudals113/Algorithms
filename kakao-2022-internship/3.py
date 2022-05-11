def solution(alp, cop, problems):
    
    global sol, visited
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    sol = 100
    visited= [0 for _ in range(len(problems))]

    def check(a, c):
        for i in range(len(problems)) :
            if problems[i][0] > a or problems[i][1] > c :
                return False
        return True
    
    def DFS(time) :
        global sol,visited
 
        if time > sol :
            return

        algo, codi = alp, cop
        
        for i in range(len(visited)) :
            algo += visited[i] * problems[i][2]
            codi += visited[i] * problems[i][3]

        if check(algo, codi) :
            sol = min(sol, time)
            return
        
        for i in range(len(problems)):
                 
            if problems[i][0] <= algo and problems[i][1] <= codi:
                visited[i] +=1
                DFS(time + problems[i][4])
                visited[i] -=1


    DFS(0)
    return sol


rst = solution(10,	10,	[[10,15,2,1,2],[20,20,3,3,4]])
# rst = solution(0	,0,	[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])
print(rst)