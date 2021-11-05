import unittest
from helpers.queue_using_stacks import QueueUsingStacks

"""
 > A Test file to test and validate the functionality of the queue
"""


class QueueUsingStacksTest(unittest.TestCase):
    queue = None

    # When queue is empty size fn should return 0
    def test_size_to_return_zero(self):
        self.queue = QueueUsingStacks()
        expected_size = 0
        result = self.queue.size()
        self.assertEqual(result, expected_size)

    # When items are added to the queue, size of the queue should change (queue grows)
    def test_enqueue(self):
        self.queue = QueueUsingStacks()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        expected_size = 4
        result = self.queue.size()
        self.assertEqual(result, expected_size)

    # When items are popped of the queue, it should retrieve in FIFO order
    def test_dequeue(self):
        self.queue = QueueUsingStacks()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        result = self.queue.dequeue()
        self.assertEqual(result, 1)
        self.assertEqual(self.queue.size(), 3)
        result = self.queue.dequeue()
        self.assertEqual(result, 2)
        self.assertEqual(self.queue.size(), 2)

    # Should return the head element (FIFO) without modifying the size of the queue
    def test_peek(self):
        self.queue = QueueUsingStacks()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        expect = 1
        result = self.queue.peek()
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
