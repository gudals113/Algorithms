# kakao-blind-2019-2.py

from re import L


def solution(record):
    
    nameDict = {}
    answer = []
    log = []
    for r in record:
        l =  list(r.split())
        if len(l)==3:
            state, uid, name =l
        else:
            state,uid = l
        
        if state == 'Enter' or state=='Change':
            nameDict[uid] = name
        
        if state =='Enter' or state=='Leave':
            log.append([state,uid])


    for state, uid in log:
        if state=='Enter':
            answer.append(nameDict[uid]+'님이 들어왔습니다.')        
        else:
            answer.append(nameDict[uid]+'님이 나갔습니다.')
    return answer