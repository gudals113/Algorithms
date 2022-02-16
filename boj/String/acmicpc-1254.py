#팰린드롬 만들기 (문자열)
s = input()
length=len(s)

max_length = 0
for i in range(1,length):
    if s[i]==s[i-1]:
        
        lengthToEnd = length-1-i
        if lengthToEnd==0:
            max_length= max(max_length,2)
            
        else:
            startIdx = i-1-(lengthToEnd)
            if startIdx >=0 :
                if s[startIdx:i] == s[length-1:i-1:-1] :
                    max_length = max(max_length,2*(lengthToEnd+1))
                
    if i>=2 and s[i]==s[i-2] :
        
        lengthToEnd= length-1-i
        
        if lengthToEnd ==0:
            max_length = max(max_length,3)
            
        else:
            startIdx = i-2 -(lengthToEnd)
            if startIdx>=0:
                if s[startIdx:i-1] == s[length-1:i-1:-1] :
                    max_length = max(max_length, 2*(lengthToEnd+1)+1)
    

if max_length==length:
    print(length)
elif max_length>=1:
    print(2*(length-max_length)+max_length)
else:
    print(2*length -1)
    
#쉽게 푸는 방법이 있다.

# s=input()
# length=len(s)

# for i in range(length):
# 	if s[i:] == s[i:][::-1] :
# 		print(length + i)
# 		break