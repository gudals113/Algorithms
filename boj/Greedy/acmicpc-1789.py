S=int(input())

tmp=1
for i in range(2, 4294967295):
    if tmp<= S < tmp+i :
        print(i-1)
        break
    else:
        tmp=tmp+i
   