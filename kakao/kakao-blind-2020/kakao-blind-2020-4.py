# kakao-blind-2020-4.py

class Node(object):
    def __init__(self, key):
        self.key = key
        self.data = {}
        self.children = {}
        self.check = 0

class Trie(object) :
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        string_len  = len(string)
        current_node = self.head
        if string_len not in current_node.data :
            current_node.data[string_len]=1
        else:
            current_node.data[string_len]+=1

        for char in string : 
            if char not in current_node.children :
                current_node.children[char] = Node(char)
                
            current_node = current_node.children[char]
            
            if string_len not in current_node.data :
                current_node.data[string_len]=1
            else:
                current_node.data[string_len]+=1
            
        current_node.check = 1
        
    def search(self,string):
        # string = 'fro??'
        global matched
        matched = 0
        current_node = self.head
        self.find(current_node, string, 0)    
        return matched

    def find(self, current_node, string, idx):
        global matched
        string_len = len(string)

        if string_len not in current_node.data:
            return
        
        if idx== len(string):
            if current_node.check ==1:
                matched+=1
            return 
        
        char =  string[idx]
        if char == '?':
            for child,_ in current_node.children.items():
                self.find(current_node.children[child], string, idx+1)
        
        elif char in current_node.children:
            self.find(current_node.children[char], string, idx+1)

        else:
            return

def solution(words, queries):
    answer = []
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    for querie in queries :
        rst = trie.search(querie)
        answer.append(rst)
    
    return answer

a = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], 
         ["fro??", "????o", "fr???", "fro???", "pro?","?????",''])
print(a)