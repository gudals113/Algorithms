def solution(alp, cop, problems):
    
    global sol, visited
  
    sol= float('inf')

    visited= [0 for _ in range(len(problems))]
    
    def check(a, c):
        for i in range(len(problems)) :
            if problems[i][0] > a or problems[i][1] > c :
                return False
        return True
    
    def DFS(idx, time, al, co) :
        global sol, visited

        if time > sol :
            return

        if check(al, co) :
            sol = min(sol, time)
            return

        for i in range(len(problems)+1):
            
            if i == len(problems) :
                DFS(idx, time+1, al+1, co)
                DFS(idx, time+1, al, co+1)
                if problems[idx][0] <= al and problems[idx][1] <= co:
                    DFS(idx, time+ problems[idx][4], al+problems[idx][2], co+problems[idx][3])
        
            
            elif i != idx and problems[i][0] <= al and problems[i][1] <= co: 
                DFS(i, time + problems[i][4], al+problems[i][2], co+problems[i][3])


    DFS(-1,0, alp, cop)

    return sol

rst = solution(10,	10,	[[10,15,2,1,2],[20,20,3,3,4]])