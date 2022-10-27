from collections import defaultdict
import math
import requests, json

### 사전 준비 ###
BASE_URL = "https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api"
PROBLEMNUM = {"problem" : 1} # 최대 200일 , 한층 20개, 3층
# PROBLEMNUM = {"problem" : 2} # 최대 1000일, 한층 200개 ,10층

def GET_AUTH_KEY():
    headers= { 'X-Auth-Token': '5509f2cfdccc615c8725d421afcb7164', 'Content-Type':'application/json' }
    start_rsp = requests.post(BASE_URL+'/start'
                    ,headers = headers
                    ,data = json.dumps(PROBLEMNUM)
                    )
    AUTH_KEY = start_rsp.json()['auth_key']
    PROBLEM = start_rsp.json()['problem']
    return AUTH_KEY, PROBLEM

# room_status = [[ [0 for _ in range(201)] for _ in range(21) ]for _ in range(4)]
AUTH_KEY,PROBLEM = GET_AUTH_KEY()
if PROBLEM==1:
    maxDay = 200
    maxRoom = 20
    maxFloor = 3
    room_status = [[ [0 for _ in range(201)] for _ in range(21) ]for _ in range(4)]
else:
    maxDay = 1000
    maxRoom = 200
    maxFloor = 10
    room_status = [[ [0 for _ in range(1001)] for _ in range(201) ]for _ in range(11)]
    
### REST API ###
def REST(method,sub,data):
    # data = {} # {'i':1,'u':2}
    if method=='GET':
        headers = { 'Authorization' : AUTH_KEY, 'Content-Type':'application/json'}
        rsp = requests.get(BASE_URL+sub, headers=headers)

    
    elif method=='POST':
        headers = { 'Authorization' : AUTH_KEY, 'Content-Type':'application/json'}
        rsp = requests.post(BASE_URL+sub, data=json.dumps(data), headers=headers)

    
    elif method=='PUT':

        headers = { 'Authorization' : AUTH_KEY, 'Content-Type':'application/json'}
        rsp = requests.post(BASE_URL+sub, data=json.dumps(data), headers=headers)

    status = rsp.status_code
    if status==200:
        return rsp.json()
    else:
        print('ERROR'. rsp.json())
        return {}

#현 재 날 짜 에 새로 들어온 예약 요청정보
def NewRequests():
    rsp = REST('GET', '/new_requests','')
    # print(rsp)
    nr = [[d['id'],d['amount'],d['check_in_date'],d['check_out_date'] ] for d in rsp['reservations_info'] ]
    return nr

#답변만 하기, 실제 배정은 simulate
def Reply(L):
    data = []
    for id, r in L:
        if r==1:
            data.append({'id':id, 'reply':'accepted'})
        elif r == 0 :
            data.append({'id':id, 'reply':'refused'})
    # print(data)
    rsp = REST('PUT','/reply', {'replies':data})
    today = rsp['day']
    return today

#실제 배정하고, 1일 진행
def Simulate(L):
    data = []
    for id, room_number in L:
        data.append({'id':id, 'room_number':room_number})
    rsp = REST('PUT','/simulate',{'room_assign':data})
    today, fail_count = rsp['day'],rsp['fail_count']
    return [today,fail_count]

def Score():
    rsp = REST('GET','/score','')  
    print(rsp)
    return rsp

#연속 배정 가능한지 체크 후, 시작 방부터 끝방 방문 처리후, 반환
def check(need, check_in, check_out):
    room_start, room_end = -1,-1
    canBook = False
    
    tmp = []
    for floor in range(1,maxFloor+1):
        if canBook:
            break
        
        tmp = []
        for r in range(1,maxRoom+1):
            
            thisRoom = True
            for day in range(check_in+1, check_out+1): # 체크인 날은 예약되어있어도 ㄱㅊ

                if room_status[floor][r][day]==0 :
                    pass
                else:
                    thisRoom= False
                    break
            
            if thisRoom :
                tmp.append([floor,r])
                if len(tmp) == need:
                    # 배정 가능!
                    canBook = True
                    break
            
            # 이 방 안되면 이전에 연속된 거 쓸모 없다.
            else:
                tmp = []

    if canBook:
        #방문 표시하기
        for floor, r in tmp:
            for day in range(check_in, check_out+1):
                room_status[floor][r][day]=1
        
        
        sA ,eA = str(tmp[0][0]), str(tmp[-1][0])
        
        if len(str(tmp[0][1]))==1:
            sBBB = '00'+str(tmp[0][1])
        elif len(str(tmp[0][1]))==2:
            sBBB='0'+ str(tmp[0][1])
        else:
            sBBB = str(tmp[0][1])
            
        if len(str(tmp[-1][1]))==1:
            eBBB = '00'+str(tmp[-1][1])
        elif len(str(tmp[-1][1]))==2:
            eBBB='0'+ str(tmp[-1][1])
        else:
            eBBB = str(tmp[-1][1])  
        
        room_start = int(sA+sBBB)
        room_end = int(eA+eBBB)

    return room_start, room_end
         


# 오늘 simulate 실제로 할 id, 시작 방 번호, 끝 방번호 저장해두기
today_in = [[] for _ in range(maxDay+1)]
final_day = [[] for _ in range(maxDay+2)]


r_c, y_c, n_c, w_c, a_c, f_c = 0,0,0,0,0,0

def plus(need,check_in, check_out, today):
    howLong = check_out-check_in + 1
    l = 1
    if PROBLEM==1:
        #방 10, 기간 1-20
        d = need/8  # 1보다 작다.
        l = 8/howLong
    elif PROBLEM==2:
        #방 50, 기간 1-100
        d= need/45
        l = 50/howLong
    val = d*l
    return val

for today in range(1,maxDay+1):
    tmp_reply = []
    tmp_simulate =[]
    
    #새로운 요청 받아오기 -> 마감 기한 리스트에 저장
    new_requests = NewRequests()
    for id, need, check_in, check_out in new_requests:
        dday = min(today+14, check_in-1)
        
        VAL = plus(need,check_in, check_out,today)
        if VAL>1: dday = today

        dday = max(dday, today)
        final_day[dday].append([id,need,check_in, check_out, VAL])

    #마감 기한 인 것들 중, 방 많이 필요한 것 순으로 정렬
    final_day[today].sort( key = lambda x: (-x[1],x[4]) )
    for id, need, check_in, check_out, VAL in final_day[today]:
        #방 배정 상태 확인 후 대답 어떻게 할 지 저장.
        room_start, room_end = check(need, check_in, check_out)
        
        if room_start != -1 :
            today_in[check_in].append([id, room_start, room_end])
            tmp_reply.append([id,1])
            
            a_c+=need
            
        else:
            tmp_reply.append([id,0])
            
            f_c += need
            
    for id, start_room_num, end_room_num in today_in[today]:
        tmp_simulate.append([id,start_room_num])

    Reply(tmp_reply)
    Simulate(tmp_simulate)

Score()
print('총 요청한 방의 수, 배정한 방 수, 거절한 방의 개수', w_c, a_c,f_c)
# print(r_count, yes_count, no_count, w_count, a_count, f_count)



