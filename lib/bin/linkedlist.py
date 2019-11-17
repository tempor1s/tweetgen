#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        return LinkedListIterator(self.head)
    
    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) Because we always keep track of the tail"""
        # Create a new node to either be set as head or as last node
        node = Node(item)
        # If head is none, set node to head and tail and then return
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.tail.next = node
        self.tail = node

    
    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) Because we always keep track of the head"""
        # Create a new node object
        node = Node(item)

        # Only enter if head does not exist
        if not self.head:
            # Use our append function because head does not exist, and it will handle tail etc
            self.append(item)
            return

        # Set our new nodes next to be our current head
        node.next = self.head
        
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
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) n being the length of the list"""
        # Standard implementation
        # count = 0
        # node = self.head
        # while node:
        #     count += 1
        #     node = node.next
        # return count
        
        # Recursive implementation
        return self._count(self.head)
    
    def _count(self, node):
        """Return the length of a linked list by traversing its nodes recursively."""
        if node is None:
            return 0
        else:
            return 1 + self._count(node.next)


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) If the head is the value we are looking for
        Worst case running time: O(n) We have to loop through the entine linked list, N being length of the linked list"""
        
        node = self.head
        
        while node:
            if quality(node.data) == True:
                return node.data
            else:
                node = node.next
        
        return None
        

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) If the head is the value we are looking for
        Worst case running time: O(n) We have to loop through the entine linked list, N being length of the linked list"""
        # Get head node and set it to a temp value, set prev to be used later
        node = self.head
        prev = None

        # If the linked list is empty, raise a value error
        if not node:
            raise ValueError(f'Item not found: {item}')
        
        # While node is not None
        while node:
            # Check if the node's data is what we are looking for
            if node.data == item:
                # item we want to remove is the head node because we have not updated the value yet
                if prev is None:
                    # Set head to be head nodes next
                    self.head = node.next
                    # if head node is also the tail node
                    if node.next is None:
                        self.tail = None
                # second case is that the item we want to remove is at the tail
                elif node.next is None:
                    # Set the previous nodes next to be none, and set it to the new tail
                    prev.next = None
                    self.tail = prev
                # third caise is that the item we want to remove is somewhere in the middle
                else:
                    # unlink the current node
                    prev.next = node.next
                # so we do not infinite loop
                return
            else:
                # node has not been found set so update temp values
                prev = node
                node = node.next
            
        # If we get to end of the loop the item does not exist, so raise value error
        raise ValueError(f'Item not found: {item}')


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
