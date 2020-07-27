from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2
def input(n):
    s = Stack()
    for i in n:
        if i =="(" or i =="{" or i == "[":
            s.push(i)
        if i ==")" or i =="}" or i == "]":
            if s.size()==0:
                return False
            if not is_match(i,s.pop()):
                return False 
    return s.size()==0  

if __name__ == "__main__":
    print(input("))"))
              
    