#Greedy

#index
#자릿수를 전부 계산해서 9부터 넣어주며 풀어야한다
alpha={}
words=[]
N= int(input())
for i in range(N):
    words.append(input())

for i in range(N):
    word = words[i]
    tenth= len(word)
    for j in range(tenth):
        
        if word[j] not in alpha:
            alpha[word[j]]= 10**(tenth-j-1)

        else:
            alpha[word[j]]+= 10**(tenth-j-1)

alpha = sorted(alpha.items(),key=lambda item:item[1], reverse=True)
ans=0
num=9
for i in range(len(alpha)):
    tmp=alpha[i]
    ans+=tmp[1]*num
    num-=1
print(ans)




#sol1 긴 순서대로 9부터 넣으면 오류 발생 ex)ABB+BB+BB+BB+BB+BB+BB+BB
# while tenth>0:
    
#     for i in range(N):
#         word = words[i]
        
#         # print(tenth)
#         if len(word)==tenth:
#             tmp=word[0-tenth]
            
#             # print(tenth, tmp)

#             if tmp not in alpha:
#                 alpha[tmp]=num
#                 ans+=num*(10**(tenth-1))
#                 num-=1
                
#             else:
#                 ans+=alpha[tmp]*(10**(tenth-1))
        
#             words[i]=word[1:]
            
#     tenth-=1
# print(alpha)
# print(ans)
