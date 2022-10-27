# 출처 - https://hudi.blog/ds-hash-table/
# Chaining
import hashlib

class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class ChainingHash:
    def __init__(self,size):
        self.size = size
        self.table = [None for _ in range(self.size)]
        
    def get_hash_val(self, key):
        if isinstance(key, int):
            return key % self.size
        
        # byte string으로 변환 후 해싱 -> 단방향 암호이므로 원래 문자열 복구 불가능.
        HASHED = hashlib.sha256(str(key).encode()) 
        
        # byte string을 16진수 문자열로 변환 -> 정수형으로 변환
        return int(HASHED.hexdigest(), 16) % self.size
    
    def add(self, key, value):
        HASH_VAL = self.get_hash_val(key)
        pointer = self.table[HASH_VAL]
        
        while pointer != None:
            # 해시 테이블에 이미 있는 key값인 경우 False 반환
            if pointer.key == key:
                return False
            pointer = pointer.next
        
        #마지막에 추가된 노드가 연결 리스트의 가장 앞에 위치
        self.table[HASH_VAL] = Node(key, value, self.table[HASH_VAL])
        return True
    
    def search(self, key):
        HASH_VAL = self.get_hash_val(key)
        pointer = self.table[HASH_VAL]
        
        while pointer!=None:
            if pointer.key == key:
                return pointer.value
            
            pointer = pointer.next
            
        return None
    
    #연결 리스트 삭제하는 방법과 동일
    def remove(self, key):
        HASH_VAL = self.get_hash_val(key)
        pointer = self.table[HASH_VAL]
        
        if pointer.key == key:
            self.table[HASH_VAL] = None
            return True
        
        while pointer.next != None:
            if pointer.next.key == key:
                break
            pointer = pointer.next
            
        #제거 대상이 없는 경우
        if pointer.next == None:
            return False
        
        pointer.next = pointer.next.next
        return True



