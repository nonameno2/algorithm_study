# 스택과 큐

# 스택
# LIFO(Last-In, First-Out)
# push peek pop


# PYTHON 스택 직접 구현
class Stack(list):
    push = list.append
    def peek(self):
        return self[-1]         


s = Stack()
s.push(1)
s.push(5)
s.push(10)
print ("my stack is: ", s)
print ("popped value is: ", s.pop())
print ("my stack is: ", s)
print ("peeked value is: ", s.peek())
print ("my stack is: ", s)


# PYTHON List를 스택으로 활용
s = []
s.append(1)
s.append(5)
s.append(10)
print ("my stack is: ", s)
print ("popped value is: ", s.pop())
print ("my stack is: ", s)
print ("peeked value is: ", s[-1])
print ("my stack is: ", s)


# 스택의 활용


# Queue
# FIFO (First-In, First-Out)
# put peek get


# PYTHON 큐 직접 구현
class Queue(list):
    put = list.append
    def peek(self):
        return self[0]
    def get(self):
        return self.pop(0)

q = Queue()
q.put(1)
q.put(5)
q.put(10)
print("my queue is: ", q)
print("removed value is: ", q.get())
print("my queue is: ", q)
print("peeked value is: ", q.peek())
print("my queue is: ", q)


# PYTHON 구현된 클래스 import
from queue import Queue
q = Queue()
q.put(1)
q.put(5)
q.put(10)
print("my queue is: ", q)
print("removed value is: ", q.get())
print("my queue is: ", q)
print("peeked value is: ", q.peek())
print("my queue is: ", q)


# PYTHON List를 큐로 활용
q = []
q.append(1)
q.append(5)
q.append(10)
print("my queue is: ", q)
print("removed value is: ", q.pop(0))
print("my queue is: ", q)
print("peeked value is: ", q[0])
print("my queue is: ", q)
