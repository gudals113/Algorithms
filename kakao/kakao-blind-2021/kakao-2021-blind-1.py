# kakao-2021-blind-1.py
def solution(new_id):

    
    #1
    new_id = new_id.lower()
    
    #2
    second_id=''
    for i in range(len(new_id)):
        asc = ord(new_id[i])
        if 97<=asc<=122 or 48<=asc<=57 or new_id[i]=='_' or new_id[i]=='-' or  new_id[i]=='.':
            second_id+=new_id[i]
    
    #3
    third_id = second_id[0]
    for i in range(1,len(second_id)):
        if second_id[i-1]=='.' and second_id[i]=='.' :
            pass
        else:
            third_id+=second_id[i]
    
    #4
    if third_id[0]=='.' : forth_id = third_id[1:]
    elif third_id[-1]=='.' : forth_id = third_id[:-1]
    else: forth_id = third_id[:]
    
    #5
    if len(forth_id)==0 : fifth_id = 'a'
    else: fifth_id = forth_id[:]
    
    #6
    if len(fifth_id)>=16:
        sixth_id = fifth_id[0:15]
    else:
        sixth_id = fifth_id[:]
        
    if sixth_id[-1] == '.' : sixth_id= sixth_id[:-1]
    
    #7
    
    if len(sixth_id)<=2 : 
        last_word= sixth_id[-1]
        last_id = sixth_id[:]+last_word
        while len(last_id)<3:
            last_id+=last_word
    else:
        last_id = sixth_id[:]        
    
    print(last_id)
    return last_id


solution("...!@BaT#*..y.abcdefghijklm") # 오답
solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p")