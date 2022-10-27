# kakao-blind-2020-4-2.py
import sys
sys.setrecursionlimit(10**5)
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

        char =  string[idx]
        
        if char == '?':
            if string_len in current_node.data:
                matched += current_node.data[string_len]
                return
            
        elif char in current_node.children:
            self.find(current_node.children[char], string, idx+1)

        else:
            return

def solution(words, queries):
    answer = []
    trie = Trie()
    reversedTrie = Trie()
    for word in words:
        trie.insert(word)
        reversedTrie.insert(word[::-1])
        
    for querie in queries :
        if querie[0]!='?':
            rst = trie.search(querie)
        else:
            rst = reversedTrie.search(querie[::-1])
        answer.append(rst)
    
    return answer

a = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], 
         ["fro??", "????o", "fr???", "fro???", "pro?"])
print(a)

b = solution(["frodo","front"],["????????"])
print(b)