#별찍기 -11
from math import log2
N = int(input())
K = int( log2(N//3) ) +1 # 총 몇 단계?
dft = ['  *  ',' * * ','*****']

def make(k):
    global dft
    
    if k ==1 :
        return 3
    
    blank = make(k-1) 

    changed=[]
    for i, line in enumerate(dft):
        changed.append(line+' '+line)
        dft[i] = ' '*(blank) + line +' '*(blank)
        
    dft = dft + changed
    
    return 3*2**(k-1)
    
make(K)

for line in dft:
    print(line)

