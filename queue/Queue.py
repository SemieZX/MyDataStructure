# Queue()
# enqueue(item) 添加元素
# deque() 从队首移除
# isEmpty()
# size()
# 每次从首位置入队，从末位置出队

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
