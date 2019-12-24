class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue(object):
    def __init__(self, order=2):
        self.order = order  # the order of the markov chain, or how much data to keep track of
        self.head = None  # head reference (will always be dequeued)
        # tail reference (this's next will always be the new item enqueued)
        self.tail = None
        self.length = 0  # to keep a reference to the length

    def __iter__(self):  # to enable for loops
        # call the QueueIter class which returns an iterator
        return QueueIter(self.head)

    def __len__(self):
        return self.length

    def enqueue(self, data):
        self.length += 1
        if self.length > self.order:  # if the length of the queue is longer than the order of markov chain requested
            self.dequeue()  # dequeue the oldest item

        if self.head is None:  # Check if the head doesnt exist
            # Create a new node with data passed in and set it to the head
            self.head = Node(data=data)
            self.tail = self.head  # Set it to the tail as well
        else:  # if the head does exist
            new_node = Node(data=data)  # create a new node
            self.tail.next = new_node  # set the current tails next to be the node we just created
            self.tail = new_node  # set the new tail to be the current node

    def dequeue(self):
        if self.head is not None:
            self.length -= 1
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    def items(self):
        node = self.head  # set node to current head
        items = []  # empty array to store all the items in the queue

        while node:  # while the node is not None
            items.append(node.data)  # append the data of the node
            node = node.next  # set the node reference to the next node

        return items  # return a list of all the items in the queue

    def serialize(self):
        # <3 Ryan
        return tuple(node.data for node in self)

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0


class QueueIter(object):
    def __init__(self, head):
        # set beginning node to be head (or whatever is passed in I guess haha)
        self.current_node = head

    def __next__(self):
        if self.current_node is not None:  # if the node is not None
            prev_node = self.current_node
            self.current_node = prev_node.next  # set node to the next node in the queue
            return prev_node  # return the nodes data on every iteration

        raise StopIteration  # stop iteration if we reach the end of the queue


if __name__ == "__main__":
    # for testing essentially
    # going to implement real tests eventually
    q = Queue(order=2)

    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    print(q.items())

    q.dequeue()

    print(q.items())

    for item in q:
        print(item)

    q.dequeue()
    q.dequeue()
    print(q.items())
    # q.dequeue()
