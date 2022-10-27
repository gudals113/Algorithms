def solution(word, pages):
    answer = 0
    word = word.lower()
    linkScore = {}
    defaultScore = [0 for _ in range(len(pages))]
    #나에게 오는 주소 이름 저장
    L = {}
    linkName = {}
     
    for idx in range(len(pages)):
        page = pages[idx]
        myInfo,page = page.split('<body>')
        
        _,myInfo = myInfo.split('<meta property="og:url" content=')
        
        myAddress=''
        if len(myInfo)>9 and myInfo[:9] =='"https://':
                for i in range(9,len(myInfo)):
                    if myInfo[i]=='"':
                        break
                    myAddress+=myInfo[i]     
        
        linkName[idx]=myAddress
        if myAddress not in L:
            L[myAddress]={}
        
        page,_ = page.split('</body>')
        l = page.split('<a href=')
        
        
        link = len(l)-1
        score = 0

        for body in l:
            if len(body)>9 and body[:9] =='"https://':
                address=''
                for i in range(9,len(body)):
                    if body[i]=='"':
    
                        if address not in L:
                            L[address]={}
                        L[address][myAddress]=1
          
                        break
                    address+=body[i]
            else:
                pass

            # print(L[address])
            
            body = body.lower()
            newBody =body.split()
            for w in newBody:
                newnewL = w.split(word)
                score+= len(newnewL)-1

        
        defaultScore[idx] = score
        linkScore[myAddress] =  score/link
    
    answerList =[]
    for idx in range(len(pages)):
        name = linkName[idx]
        myScore = defaultScore[idx]
        for other,_ in L[name].items():
            myScore += linkScore[other]
            
        answerList.append([ myScore, idx])
        
    answerList.sort(key = lambda x:(-x[0],x[1]))
    # print(defaultScore)
    # print(answerList)
    answer = answerList[0][1]
    return answer



# print('---'*10)
# solution("blind",['<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://a.com"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href="https://b.com"> Link to b </a>\n</body>\n</html>', '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://b.com"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href="https://a.com"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href="https://c.com"> Link to c </a>\n</body>\n</html>', '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://c.com"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href="https://a.com"> Link to a </a>\n</body>\n</html>'])
# solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])