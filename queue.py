class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self, value):
        self.queue.pop()

    def print_queue(self):
        for val in self.queue:
            print(val)


q = Queue()

q.enqueue(10)

q.enqueue('cat')

q.enqueue([1,2,3])

q.print_queue()