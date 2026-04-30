
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, num):
        new_node = Node(num)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        self.node_num += 1

    def push_back(self, num):
        new_node = Node(num)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = None

        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            print("List Empty")

        elif self.head.next == None:
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0

            return temp.data
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.node_num -= 1
            return temp.data
    
    def pop_back(self):
        if self.tail == None:
            print("List Emtpy")

        elif self.tail.prev == None:
            temp = self.tail

            self.tail = None
            self.head = None
            self.node_num = 0
        
            return temp.data

        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.node_num -= 1
            return temp.data
    
    def size(self):
        return self.node_num
    
    def empty(self):
        return 1 if self.node_num == 0 else 0
    
    def front(self):
        if self.head == None:
            print("List is empty")
        else:
            return self.head.data
    
    def back(self):
        if self.tail == None:
            print("List is empty")
        else:
            return self.tail.data


N = int(input())

new_list = DoubleLinkedList()
for _ in range(N):
    line = input().split()

    if line[0] == "push_front":
        new_list.push_front(line[1])
    elif line[0] == "push_back":
        new_list.push_back(line[1])
    elif line[0] == "pop_front":
        print(new_list.pop_front())
    elif line[0] == "pop_back":
        print(new_list.pop_back())
    elif line[0] == "size":
        print(new_list.size())
    elif line[0] == "empty":
        print(new_list.empty())
    elif line[0] == "front":
        print(new_list.front())
    elif line[0] == "back":
        print(new_list.back())
        