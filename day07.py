from operator import itemgetter


class Stack:
    def __init__(self):
        self.items = list()

    def push(self,data):
        self.items.append(data)

    def pop(self) -> object:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> object:
        return self.items[-1]

    def is_empty(self)-> bool:
        return len(self,items) == 0

s1 = Stack()
s1.push(-9)
s1.push(11)
s1.push(977)
print(s1.pop())
# pop은 삭제하므로 977이 삭제됨
print(s1.peek())
print(s1.peek())
# 후입선출로 마지막에 들어간 숫자가 peek됨
print(s1.is_empty())



