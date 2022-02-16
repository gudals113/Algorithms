#생태학 
# dic={}
# count=0
# while True:
#     try:
#         word= input()
#         count+=1
#         if word in dic:
#             dic[word]+=1
#         else:
#             dic[word]=1
            
#     except:
#         break
    
# for word in dic:
#     dic[word] = round(dic[word]/count*100 , 4)

# sorted_dic = sorted(dic.items())

# for info in sorted_dic :
#     print(f'{info[0]} {info[1]:.4f}')

import sys
line = sys.stdin.readline
dic={}
count=0
while True:
    word = line().rstrip()
    if not word:
        break
    count+=1
    if word in dic:
        dic[word]+=1
    else:
        dic[word]=1

for word in dic:
    dic[word] = round(dic[word]/count*100 , 4)

sorted_dic = sorted(dic.items())

for info in sorted_dic :
    print(f'{info[0]} {info[1]:.4f}')