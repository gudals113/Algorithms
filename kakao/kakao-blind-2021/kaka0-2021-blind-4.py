# kaka0-2021-blind-4.py
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = []
        self.children = {}

def solution(info, query):
    
    def find(current, qlist, idx):
        
        if idx==len(qlist)-1:
            scoreList = current.data
            # print(scoreList)
            target = qlist[-1]
            s,e=-1,len(scoreList)
            count = 0        
                
            while e-s>1:
                mid = (s+e)//2
                if scoreList[mid] >= target:
                    e=mid
                    count = len(scoreList)-mid
                elif scoreList[mid]<target:
                    s = mid
            
            return count

    
        if qlist[idx]=='-':
            tmp = 0
            for child,_ in current.children.items():
                
                tmp+=find(current.children[child],qlist,idx+1)
            
        else:

            current = current.children[qlist[idx]]
            tmp = find(current, qlist,idx+1)
    
        return tmp
    
    answer = []    
    root = Node(None)
    lan = ['java','python','cpp']
    job = ['backend','frontend']
    lon = ['junior','senior']
    food = ['pizza','chicken']
    
    for l in lan:
        root.children[l]=Node(l)
        node = root.children[l]
        for j in job:
            node.children[j]=Node(j)
            node2 = node.children[j]
            for lo in lon:
                node2.children[lo]=Node(lo)
                node3 = node2.children[lo]
                for f in food:
                    node3.children[f] = Node(f)
    for i in info:
        l,j,lo, f, score = i.split()
        score = int(score)
        root.data.append(score)
        
        lanNode = root.children[l]
        lanNode.data.append(score)
        
        jobNode = lanNode.children[j]
        jobNode.data.append(score)
        
        loNode = jobNode.children[lo]
        loNode.data.append(score)
        
        foodNode = loNode.children[f]
        foodNode.data.append(score)
        
    for l in lan:
        node = root.children[l]
        for j in job:
            node2 = node.children[j]
            for lo in lon:
                node3 = node2.children[lo]
                for f in food:
                    node4 = node3.children[f]
                    node4.data.sort()
                    
    for q in query:
        qlist = q.split(' and ')
        food,score =  qlist[-1].split()
        qlist.pop()
        qlist.append(food)
        qlist.append(int(score))

        # print('find Start', qlist)
        rst = find(root,qlist,0)
        answer.append(rst)

    print(answer)
    return answer

# solution(['java backend junior pizza 150', 'java backend junior pizza 100'],['java and backend and junior and pizza 150'])
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])



    