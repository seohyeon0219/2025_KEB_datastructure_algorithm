import random


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        current.next = Node(data)

    def search(self, target) -> bool:
        return False


    def __str__(self):
        return "end"



if __name__ == "__main__":
    l = LinkedList()
    i = 0
    while i < 20:
        n = random.randint(1, 20)
        l.append(n)
        print(n, end=' ')
        i = i + 1
    #print(l)
    print(l.search(10))