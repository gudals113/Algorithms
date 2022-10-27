from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    whoReportMe ={}
    answerDict = {}
    for user in id_list:
        whoReportMe[user] = defaultdict(int)
        answerDict[user] = 0
        
    for r in report:
        reporting,reported = r.split()
        whoReportMe[reported][reporting]+=1
    
    for user in id_list:
        if len(whoReportMe[user]) >=k:
            for reporting,_ in whoReportMe[user].items():
                answerDict[reporting]+=1
            
        
    for i in range(len(id_list)):
        answer.append(answerDict[id_list[i]])
        
    return answer

solution(["muzi", "frodo", "apeach", "neo"]	,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	,2)