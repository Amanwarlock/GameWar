"""
 > Implementation of queue using stacks - FIFO
"""


class QueueUsingStacks:
    oldest_stack = None
    newest_stack = None

    def __init__(self):
        self.oldest_stack = []
        self.newest_stack = []

    # Returns the size/length of the queue
    def size(self):
        return len(self.oldest_stack) + len(self.newest_stack)

    # Function maintains FIFO order by shifting the newest stack to the oldest stack tail first
    def shift_stacks(self):
        if len(self.oldest_stack) == 0:
            while len(self.newest_stack) > 0:
                self.oldest_stack.append(self.newest_stack.pop())

    # Adds items at the head of the queue
    def enqueue(self, item):
        self.newest_stack.append(item)

    # Retrieves items from the head of the queue - FIFO
    def dequeue(self):
        self.shift_stacks()
        return self.oldest_stack.pop()

    # Returns the head of the queue. After this operation the queue size does not change
    def peek(self):
        self.shift_stacks()
        return self.oldest_stack[-1]
