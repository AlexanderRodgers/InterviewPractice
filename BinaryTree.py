from queue import Queue 

class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            prev = current
            while current:
                prev = current
                if current.value < value:
                    current = current.right
                else:
                    current = current.left
            if prev.value < value:
                prev.right = Node(value)
            else:
                prev.left = Node(value)

    def line_by_line(self):
        line_order = [] 
        q = Queue()
        if not self.root:
            q.enqueue(self.root)
            self.bfs(q, line_order)

    def bfs(self, queue, line_order):
        
        while not queue.is_empty():
            node = queue.dequeue()
            line_order.append(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.left:
                queue.enqueue(node.right)
            



    def in_order(self):
        node = self.root
        self.in_order_helper(node)
    
    def in_order_helper(self, node):
        if node:
            self.in_order_helper(node.left)
            print(node.value)
            self.in_order_helper(node.right)

    def pre_order(self):
        node = self.root
        self.pre_order_helper(node)

    def pre_order_helper(self, node):
        if node:
            print(node.value)
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    def post_order(self):
        node = self.root
        self.post_order_helper(node)
    
    def post_order_helper(self, node):
        if node:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(node.value)
