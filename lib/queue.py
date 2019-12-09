class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue(object):
    def __init__(self, order=2):
        self.order = order # the order of the markov chain, or how much data to keep track of
        self.head = None # head reference (will always be dequeued)
        self.tail = None # tail reference (this's next will always be the new item enqueued)
        self.length = 0 # to keep a reference to the length
    
    def __iter__(self): # to enable for loops
        return QueueIter(self.head) # call the QueueIter class which returns an iterator
    
    def __str__(self):
        return " ".join(self)
    
    def enqueue(self, data):
        if self.length > self.order: # if the length of the queue is longer than the order of markov chain requested
            self.dequeue() # dequeue the oldest item
        
        if self.head == None: # Check if the head doesnt exist
            self.head = Node(data) # Create a new node with data passed in and set it to the head
            self.tail = self.head # Set it to the tail as well
        else: # if the head does exist
            node = Node(data) # create a new node
            self.tail.next = node # set the current tails next to be the node we just created
            self.tail = node # set the new tail to be the current node 

    def dequeue(self):
        if self.head:
            head = self.head # current head node
            self.head = self.head.next # set the head to be the next item in the queue
            self.length -= 1 # decrease the length
            if self.tail == None: # check to see if the tail is none
                self.tail = None # 
            return head.data # return the data of the dequed node
        raise Exception('Tried to dequeue an item from an empty queue.')

    def items(self):
        node = self.head # set node to current head
        items = [] # empty array to store all the items in the queue

        while node: # while the node is not None
            items.append(node.data) # append the data of the node
            node = node.next # set the node reference to the next node
        
        return items # return a list of all the items in the queue
    
    # def serialize(self):
    #     # <3 Ryan
    #     return tuple(node.data for node in self)


class QueueIter(object):
    def __init__(self, head):
        self.node = head # set beginning node to be head (or whatever is passed in I guess haha)
    
    def __next__(self):
        if self.node: # if the node is not None
            prev = self.node
            self.node = prev.next # set node to the next node in the queue
            return prev.data # return the nodes data on every iteration

        raise StopIteration # stop iteration if we reach the end of the queue


if __name__ == "__main__":
    # for testing essentially
    # going to implement real tests eventually
    q = Queue(order=2)

    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    print(q.items())
    item = q.dequeue()
    print(item.data)
    print(q.items())

    for item in q:
        print(item)
    
    q.dequeue()
    q.dequeue()
    print(q.items())
    # q.dequeue()