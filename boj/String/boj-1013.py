#Contact (String)
def check(TC):
    idx=0
    status='0'

    while True:
        if status=='0':
            if idx==len(TC):
                return -1
        
            if TC[idx]==status :
                idx+=1
            else:
                idx+=1
                status='1'
                
        else :
            if idx==len(TC):
                return idx
            
            if TC[idx]==status:
                idx+=1
                
            else:
                
                if TC[idx-2:idx+2]=='1100':
                    return idx-1
                
                else :
                    return idx
                
                
                
T=int(input())
for _ in range(T):
    TC = input()
    while True:
        # print(TC)
        
        if len(TC)==0:
            print('YES')
            break
            
        if TC[:2]=='01' :
            TC=TC[2:]
            
        elif TC[:3]=='100':
            TC=TC[2:]
            idx = check(TC)
            
            if idx==-1:
                print('NO')
                break
            
            else:
                TC=TC[idx:]
            
        else:
            print('NO')
            break

