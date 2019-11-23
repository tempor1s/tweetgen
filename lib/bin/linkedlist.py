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
        self.size = 0  # length optimization
        # Append given items
        if items:
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
        # set node to head
        node = self.head
        # loop through every item in the linked list
        for _ in range(len(self)):
            # yield the data, then traverse to the next item in the linked list
            yield node.data
            # traverse to the next item in the node
            node = node.next
        # return LinkedListIterator(self.head)

    def __len__(self):
        # we calculate size in other functions, so this just will return that value
        return self.size

    def __contains__(self, data):
        # because we implemented __iter__ we can loop through self to get the data
        for node_data in self:
            if node_data == data:
                return True

        return False

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) Because we always keep track of the tail"""
        # Create a new node to either be set as head or as last node
        node = Node(item)
        # If head is none, set node to head and tail and then return
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return

        self.tail.next = node
        self.tail = node
        self.size += 1  # increment size by 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) Because we always keep track of the head"""
        # Create a new node object
        node = Node(item)

        # Only enter if head does not exist
        if self.head is None:
            # Use our append function because head does not exist, and it will handle tail etc
            self.append(item)
            return

        # Set our new nodes next to be our current head
        node.next = self.head
        # set the new head to be our new node
        self.head = node
        self.size += 1  # increment size by 1

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
        """Return a boolean indicating whether this linked list is empty.
        Running time: O(1) because it just checks if the head node exists"""
        return self.head is None

    def length(self):
        """Return the length of this list
        Running time: O(1) because we calculate length in other functions"""
        # Standard implementation
        # count = 0
        # node = self.head
        # while node:
        #     count += 1
        #     node = node.next
        # return count

        # Recursive implementation
        # return self._count(self.head)

        return self.size

    def _count(self, node):
        """Return the length of a linked list by traversing its nodes recursively."""
        if node is None:
            return 0
        else:
            return 1 + self._count(node.next)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) If the head or tail is the value we are looking for
        Worst case running time: O(n) We have to loop through the entine linked list, N being length of the linked list"""
        # Check head and tail data first before looping to increase potential time
        if quality(self.head.data) == True:
            return self.head.data
        
        if quality(self.tail.data) == True:
            return self.tail.data

        node = self.head
        while node:
            if quality(node.data) == True:
                return node.data
            else:
                node = node.next

        return None

    def replace(self, item, new_item):
        """Replace the given item from this linked list.
        Best case running time: O(1) If the head is the value we are looking for
        Worst case running time: O(n) We have to loop through the entine linked list, N being length of the linked list"""
        # TODO: Check if head and tail are the nodes first before looping to increase potential time
        node = self.head

        while node:
            if node.data == item:
                node.data = new_item
                return

            node = node.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) If the head is the value we are looking for
        Worst case running time: O(n) We have to loop through the entine linked list, N being length of the linked list"""
        # Get head node and set it to a temp value, set prev to be used later
        node = self.head
        prev = None

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
                # reduce the size by 1 because we just deleted an item
                self.size -= 1
                # so we do not infinite loop
                return
            else:
                # node has not been found set so update temp values
                prev = node
                node = node.next

        # If we get to end of the loop the item does not exist, so raise value error
        raise ValueError(f'Item not found: {item}')


class LinkedListIterator(object):
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item


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
