# Doubly LinkedList Implementation
class Node(object):
    def __init__(self):
        self.next = None
        self.previous = None
        self.element = None
     
class LinkedList(object):
    def __init__(self):
        self.n = 0
        self.last = Node()
        self.first = self.last
         
    def append(self, element):
        self.last.element = element
        self.last.next = Node()
        tmp = self.last
        self.last = self.last.next
        self.last.previous = tmp
        self.n += 1
     
    def front(self):
        if self.n == 0: return None
        e = self.first.element
        self.first = self.first.next
        self.n -= 1
        return e
         
    def back(self):
        if self.n == 0: return None
        e = self.last.previous.element
        self.last = self.last.previous
        self.last.next = Node()
        self.n -= 1
        return e
         
    def size(self):
        return self.n
     
    def elements(self):
        i = self.first
        while i.element:
            yield i.element
            i = i.next
