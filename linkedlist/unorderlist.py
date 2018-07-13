# list()
# add(item)
# remove(item)
# search(item)
# isEmpty()
# size()
# append(item) 添加到最后
# insert(pos,item)
# pop()
# pop(pos)

# define the node class
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
      
    def getNext(self):
        return self.next
      
    def setData(self,newdata):
        self.data = newdata
        
    def setNext(self,newnext):
        self.next = newnext
  
  # define Unordered List class
  class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


    def remove(self,item):
        # initial
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current 
                current = current.getNext()

        if previous == None: #首元素命中
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
  
    
