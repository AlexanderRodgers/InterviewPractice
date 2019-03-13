class Node:

    def __init__(self, val):
        self.value = val
        self.next = None

class Stack:

    def __init__(self):
        self.root = None
        self.size = 0

    def push(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            temp = self.root
            self.root = Node(val)
            self.root.next = temp
        self.size += 1

    def pop(self):
        if not self.root:
            print('nothing to pop')
        else:
            temp = self.root
            self.root = self.root.next
            self.size -= 1
            return temp.value

    def peek(self):
        if not self.root:
            print('no values')
        else:
            return self.root

    def print_vals(self):
        node = self.root
        while node:
            print(node.value)
            node = node.next

    def is_empty(self):
        return self.size == 0
