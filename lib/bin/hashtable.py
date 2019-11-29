from linkedlist import LinkedList
# from lib.utils import time_it


# This is my implementation using seperate chaining collision resolution
class HashTable(object):
    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def __contains__(self, key):
        return self.contains(key)

    def __len__(self):
        return self.length()

    def __iter__(self):
        for bucket in self.buckets:
            for item in bucket.items():
                yield item
    
    # @time_it
    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    # @time_it
    def _get_item(self, key):
        """Return item and bucket for a given key.
        Params:
            key: object - the key you want to get the item from

        Returns:
            item, bucket:
                Item: The item that was requested, None if not found
                Bucket: The bucket that the item was searched for in (linked list)
        """
        # get the bucket index for the given key
        bucket_index = self._bucket_index(key)
        # get the bucket (linked list) with the bucket index we just got
        bucket = self.buckets[bucket_index]
        # find the item from the given key
        item = bucket.find(lambda item: item[0] == key)
        # return the item, bucket
        return item, bucket

    # @time_it
    def keys(self):
        """Return a list of all keys in this hash table.
        Average case running time: O(N) Every bucket only has 1 item
        Worst case running time: O(N) We loop through every bucket, and then every item in each bucket"""
        # create an empty list to store all keys
        # all_keys = []
        # loop through each bucket
        for bucket in self.buckets:
            # append each key that is in each item (linked list) in the bucket
            for key, value in bucket.items():
                # all_keys.append(key)
                yield key
        # return a list of all the keys
        # return all_keys

    # @time_it
    def values(self):
        """Return a list of all values in this hash table.
        Average case running time: O(N) Every bucket only has 1 item
        Worst case running time: O(N) We loop through every bucket, and then every item in each bucket"""
        # create an empty list to store all values
        all_values = []
        # loop through each bucket
        for bucket in self.buckets:
            # append each value that is in each item (linked list) in the bucket
            for key, value in bucket.items():
                all_values.append(value)
        # return a list of all the values
        return all_values

    # @time_it
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Average case running time: O(N) Every bucket only has 1 item
        Worst case running time: O(N) Every bucket has multiple items"""
        # create an empty list to store items
        all_items = []
        # loop through each bucket
        for bucket in self.buckets:
            # extend all_items list with all the items from each bucket
            all_items.extend(bucket.items())
        # return a list of all the items
        return all_items

    # @time_it
    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Average case running time: O(1) We calculate length in our set and delete functions"""
        # create temporary variable to store count
        # count = 0
        # # loop through each bucket
        # for bucket in self.buckets:
        #     # for every item in each bucket, increment count by 1
        #     for item in bucket.items():
        #         count += 1
        # # return the count
        # return count
        return self.size

    # @time_it
    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Average case running time: O(1) Every bucket has 1 item
        Worst case running time: O(N) If too many items are hashed in a bucket."""
        # get item and bucket
        item, bucket = self._get_item(key)

        # if item is not None
        if item:
            return True
        return False

    # @time_it
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Average case running time: O(1) Every bucket has 1 item
        Worst case running time: O(N) If too many items are hashed in a bucket."""
        # get item and bucket
        item, bucket = self._get_item(key)

        # if item exists return the value associated with the key. otherwise raise KeyError if item was not found
        if item:
            return item[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    # @time_it
    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Average case running time: O(1) Every bucket has 1 item
        Worst case running time: O(N) If too many items are hashed in a bucket."""
        # get the item and the bucket
        item, bucket = self._get_item(key)

        # if item exists, replace it with item. otherwise append it to that bucket
        if item:
            bucket.replace(item, (key, value))
        else:
            bucket.append((key, value))
            self.size += 1

    # @time_it
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Average case running time: O(1) Every bucket has 1 item
        Worst case running time: O(N) If too many items are hashed in a bucket."""
        # get the item and the bucket
        item, bucket = self._get_item(key)

        # if item exists, delete it. otherwise raise KeyError that item was not found
        if item:
            bucket.delete(item)
            self.size -= 1
        else:
            raise KeyError('Key not found: {}'.format(key))

    # @time_it
    def clear(self):
        """Delete all items from this hash table.
        Average case running time: O(N) Looping through every item in every bucket
        """
        # loop through every bucket
        for bucket in self.buckets:
            # for every item in bucket, delete it
            for key, value in bucket.items():
                self.delete(key)
    
    # @time_it
    def reversed(self):
        """Return a reverse iterator over the keys of the dictionary. This is a shortcut for reversed(d.keys())"""
        return reversed(self.keys())


# This is my implementation using linear probing collision resolution
# class LinearHashTable(object):
#     def __init__(self, init_size=8):
#         """Initialize this hash table with the given initial size."""
#         # Create a new list (used as fixed-size array) of empty lists
#         self.buckets = [[] for _ in range(init_size)]
#         self.size = 0

#     def __str__(self):
#         """Return a formatted string representation of this hash table."""
#         items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
#         return '{' + ', '.join(items) + '}'

#     def __repr__(self):
#         """Return a string representation of this hash table."""
#         return 'HashTable({!r})'.format(self.items())
    
#     def __contains__(self, key):
#         return self.contains(key)

#     def __len__(self):
#         return self.length()

#     def _bucket_index(self, key):
#         """Return the bucket index where the given key would be stored."""
#         # Calculate the given key's hash code and transform into bucket index
#         return hash(key) % len(self.buckets)
    
#     def _get_item(self, key):
#         bucket_index = self._bucket_index(key)
#         bucket = self.buckets[bucket_index]
#         return bucket

#     def keys(self):
#         """Return a list of all keys in this hash table.
#         Average case running time: O(N) Every bucket only has 1 item
#         Worst case running time: O(N^2) We loop through every bucket, and then every item in each bucket"""
#         for bucket in self.buckets:
#             for item in bucket:
#                 yield item[0]

#     def values(self):
#         """Return a list of all values in this hash table.
#         Average case running time: O(N) Every bucket only has 1 item
#         Worst case running time: O(N^2) We loop through every bucket, and then every item in each bucket"""
#         for bucket in self.buckets:
#             for item in bucket:
#                 yield item[1]

#     def items(self):
#         """Return a list of all items (key-value pairs) in this hash table.
#         Average case running time: O(N) Every bucket only has 1 item
#         Worst case running time: O(N^2) Every bucket has multiple items"""
#         # create an empty list to store items
#         all_items = []
#         # loop through each bucket
#         for bucket in self.buckets:
#             # extend all_items list with all the items from each bucket
#             all_items.extend(bucket[0])
#         # return a list of all the items
#         return all_items
    
#     def length(self):
#         return self.size

#     def contains(self, key):
#         bucket = self._get_item(key)
#         if bucket:
#             return True
#         return False

#     def get(self, key):
#         bucket = self._get_item(key)
#         if bucket:
#             return bucket[0][1]
#         else:
#             raise KeyError(f'Key not found: {key}')

#     def set(self, key, value):
#         bucket = self._get_item(key)

#         # if bucket is not empty
#         if bucket:
#             bucket[0] = (key, value)
#         else:
#             bucket.append((key, value))
#             self.size += 1

#     def delete(self, key):
#         bucket = self._get_item(key)

#         if bucket:
#             bucket.pop(0)
#             self.size -= 1
#         else:
#             raise KeyError(f'Key not found: {key}')

#     def clear(self, key):
#         for bucket in self.buckets:
#             bucket.pop(0)

#     def reversed(self):
#         pass


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


if __name__ == '__main__':
    test_hash_table()
