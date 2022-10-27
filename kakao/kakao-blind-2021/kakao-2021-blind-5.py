# kakao-2021-blind-5.py
def solution(play_time, adv_time, logs):
    h,m,sec =map(int, play_time.split(':'))
    ah,am,asec = map(int, adv_time.split(':'))
    m+=h*60
    sec+=m*60
    am+=ah*60
    asec+=am*60
    print(sec,asec)
    
    answer = ''
    return answer
    
solution('99:99:99','10:01:00',[])