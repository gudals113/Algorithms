# 전화번호 목록 
# 트라이로 풀이
# 220831
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
    
class Trie(object) :
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        current_node = self.head
        
        for char in string : 
            if char not in current_node.children :
                current_node.children[char] = Node(char)
                
            current_node = current_node.children[char]
        
        current_node.data = string
        
    def search(self,string):
        current_node = self.head
        for char in string:
            if current_node.data != None:
                return True

            if char in current_node.children:
                current_node = current_node.children[char]
            
            else:
                return False
        return False
            
T = int(input())
for _ in range(T):
    N = int(input())
    p_num_list = []
    trie = Trie()
    
    for _ in range(N):
        p_num = input()
        p_num_list.append(p_num)   
    
        trie.insert(p_num)
    
    answer ='YES'
    for p_n in p_num_list:
        if trie.search(p_n) :
            answer = 'NO'
    
    print(answer)


