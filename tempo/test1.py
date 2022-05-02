def solution(purchase):
    start=[ 0, 1, 1+31, 1+31+28, 1+31+28+31, 1+31+28+31+30, 1+31+28+31+30+31, 1+31+28+31+30+31+30, 1+31+28+31+30+31+30+31, 1+31+28+31+30+31+30+31+31,1+31+28+31+30+31+30+31+31+30, 1+31+28+31+30+31+30+31+31+30+31, 1+31+28+31+30+31+30+31+31+30+31+30]
    answer = [0 for _ in range(5)]
    
    cal=[ 0 for _ in range(400) ]
    for info in purchase:
        when = info[5:10].split('/')
        
        month, date=int(when[0]) , int(when[1])
        price = int(info[11:])
        
        for i in range(30):
            s = start[month]+date-1+i
            cal[s]+=price
    
    
    for i in range(1,366):
        if cal[i]<10000:
            answer[0]+=1
        elif cal[i]<20000 and cal[i]>=10000:
            answer[1]+=1
        elif cal[i]<50000 and cal[i]>=20000:
            answer[2]+=1
        elif cal[i]<100000 and cal[i]>=50000:
            answer[3]+=1
        elif cal[i]>=100000:
            answer[4]+=1
    print(answer)    
    return answer


solution(["2019/01/01 5000", "2019/01/20 15000", "2019/12/31 90000"])