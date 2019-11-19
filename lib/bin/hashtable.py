from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Average case running time: O(N) Every bucket only has 1 item
        Worst case running time: O(N^2) We loop through every bucket, and then every item in each bucket"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Average case running time: O(N) Every bucket only has 1 item
        Worst case running time: O(N^2) We loop through every bucket, and then every item in each bucket"""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Average case running time: O(N) Every bucket only has 1 item
        Worst case running time: O(N^2) Every bucket has multiple items"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Average case running time: O(N) Every bucket only has 1 item
        Worst case running time: O(N^2) We loop through every bucket, and then every item in each bucket"""
        # TODO: Create an implementation that stores length in the hashtable and lets the functions increment / decremt it
        count = 0
        for bucket in self.buckets:
            for item in bucket.items():
                count += 1
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Average case running time: O(1) Every bucket has 1 item
        Worst case running time: O(N) N being the amount of items in a bucket"""
        bucket_index = self._bucket_index(key)

        # get the bucket (linked list) with the bucket index we just got
        bucket = self.buckets[bucket_index]

        if bucket.find(lambda item: item[0] == key):
            return True

        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Average case running time: O(1) Every bucket has 1 item
        Worst case running time: O(N) N being the amount of items in a bucket"""
        # get the bucket index for the given key
        bucket_index = self._bucket_index(key)

        # get the bucket (linked list) with the bucket index we just got
        bucket = self.buckets[bucket_index]

        item = bucket.find(lambda item: item[0] == key)

        if item:
            # returns the value associated with the key
            return item[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Average case running time: O(1) Every bucket has 1 item
        Worst case running time: O(N) Having to loop through N items in a bucket to find the item to replace"""
        # get the bucket index for the given key
        bucket_index = self._bucket_index(key)

        # get the bucket (linked list) with the bucket index we just got
        bucket = self.buckets[bucket_index]

        # if an item with that key is found
        item = bucket.find(lambda item: item[0] == key)
        if item:
            bucket.replace(item, (key, value))
        else:  # insert given key-value entry into bucket if not found
            bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Average case running time: O(1) Every bucket has 1 item
        Worst case running time: O(N) N being amount of items in a bucket"""
        # get the bucket index for the given key
        bucket_index = self._bucket_index(key)

        # get the bucket (linked list) with the bucket index we just got
        bucket = self.buckets[bucket_index]

        item = bucket.find(lambda item: item[0] == key)

        if item:
            bucket.delete(item)
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


def test():
    ht = HashTable()
    print('hash table: {}'.format(ht))
    ht.set('hello', 1)
    ht.get('hello')


if __name__ == '__main__':
    test_hash_table()
    # test()
