#!python

from lib.queue import Queue
import unittest

class QueueTest(unittest.TestCase):
    def test_add_item(self):
        q = Queue()

        q.enqueue('A')

        assert len(q) == 1
        assert q.head.data == 'A'
        assert q.tail.data == 'A'
    
    def test_len(self):
        q = Queue()
        
        assert len(q) == 0
        q.enqueue('A')
        assert len(q) == 1
        q.enqueue('B')
        assert len(q) == 2
        q.dequeue()
        assert len(q) == 1
        q.dequeue()
        assert len(q) == 0
    
    def test_dequeue(self):
        q = Queue()

        q.enqueue('A')
        assert len(q) == 1
        assert q.head.data == 'A'
        assert q.tail.data == 'A'
        q.enqueue('B')
        assert len(q) == 2
        assert q.head.data == 'A'
        assert q.tail.data == 'B'
        q.dequeue()
        assert len(q) == 1
        assert q.head.data == 'B'
        assert q.tail.data == 'B'
    
    def test_items(self):
        q = Queue()

        q.enqueue('A')
        q.enqueue('B')

        assert ['A', 'B'] == q.items()
    
    def test_serialize(self):
        q = Queue()

        q.enqueue('A')
        q.enqueue('B')

        items = q.serialize()

        assert tuple(['A', 'B']) == items
    
    def test_iteration(self):
        q = Queue()

        items = ['A', 'B']

        for item in items:
            q.enqueue(item)
        
        for i, item in enumerate(q):
            assert item.data == items[i]