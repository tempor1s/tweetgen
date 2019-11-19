class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return 'Node({!r})'.format(self.data)
    

class DoubleyLinkedList(object):
    def __init__(self, items=None):
        self.head = None
        self.tail = None

        if items:
            for item in items:
                self.append(item)
    

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'DoubleyLinkedList({!r})'.format(self.items())

    def append(self, item):
        # Create new node with given data
        node = Node(item)

        # Edge case for if the head does not exist
        if self.head is None:
            self.head = node
            self.tail = node
            return
        # Set the tails next to be the new node
        self.tail.next = node
        # Set the tails prev to be the old tail
        self.tail.prev = self.tail
        # Set the new tail to be the node
        self.tail = node
    
    def prepend(self, item):
        # create a new node with the data passed in
        node = Node(item)

        # if the head does not exist
        if self.head is None:
            # use our append function because head does not exist, and it will handle tail etc
            self.append(item)
            return

        # set out nodes next to be our current head
        node.next = self.head
        # set the current head to have a previous of our new node
        self.head.prev = node
        # set the new head to be our new node
        self.head = node
    
    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list
    
    def is_empty(self):
        return self.head is None
    
    def length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    def find(self, quality):
        node = self.head

        while node:
            if quality(node.data) == True:
                return node
            else:
                node = node.next
        
        return None
    
    def replace(self, item, new_item):
        node = self.head

        while node:
            if node.data == item:
                node.data == new_item
                return
            
            node = node.next
        
    def delete(self, item):
        pass