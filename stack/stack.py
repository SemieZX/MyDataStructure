# Stack()
# push(item) 入栈
# pop() 弹出栈顶元素
# peek() 返回栈顶元素，但不弹出
# isEmpty() 
# size（）


# define a Stack class

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items(len(items)-1)

    def size(self):
        return len(self.items)
