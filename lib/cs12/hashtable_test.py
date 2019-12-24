from hashtable import HashTable
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class HashTableTest(unittest.TestCase):

    def test_init(self):
        ht = HashTable(4)
        assert len(ht.buckets) == 4
        assert ht.length() == 0

    def test_keys(self):
        ht = HashTable()
        assert list(ht.keys()) == []
        ht.set('I', 1)
        assert list(ht.keys()) == ['I']
        ht.set('V', 5)
        self.assertCountEqual(list(ht.keys()), ['I', 'V'])  # Ignore item order
        ht.set('X', 10)
        self.assertCountEqual(list(ht.keys()), ['I', 'V', 'X'])  # Ignore item order

    def test_values(self):
        ht = HashTable()
        assert list(ht.values()) == []
        ht.set('I', 1)
        assert list(ht.values()) == [1]
        ht.set('V', 5)
        self.assertCountEqual(list(ht.values()), [1, 5])  # Ignore item order
        ht.set('X', 10)
        self.assertCountEqual(list(ht.values()), [1, 5, 10])  # Ignore item order

    # my test
    def test_sum_values(self):
        ht = HashTable()
        assert len(ht.values()) == 0
        ht.set('A', 3)
        assert len(ht.values()) == 1
        ht.set('B', 5)
        assert len(ht.values()) == 2
        # check sum of values to make sure they are returning ints
        assert sum(ht.values()) == 8

    def test_items(self):
        ht = HashTable()
        assert ht.items() == []
        ht.set('I', 1)
        assert ht.items() == [('I', 1)]
        ht.set('V', 5)
        self.assertCountEqual(ht.items(), [('I', 1), ('V', 5)])
        ht.set('X', 10)
        self.assertCountEqual(ht.items(), [('I', 1), ('V', 5), ('X', 10)])

    def test_length(self):
        ht = HashTable()
        assert ht.length() == 0
        ht.set('I', 1)
        assert ht.length() == 1
        ht.set('V', 5)
        assert ht.length() == 2
        ht.set('X', 10)
        assert ht.length() == 3
    
    # my test
    def test_len_function(self):
        ht = HashTable()
        assert len(ht) == 0
        ht.set('I', 1)
        assert len(ht) == 1
        ht.set('V', 5)
        assert len(ht) == 2
        ht.set('X', 10)
        assert len(ht) == 3
    
    # my test
    def test_length_after_delete(self):
        ht = HashTable()
        assert len(ht) == 0
        ht.set('A', 1)
        assert len(ht) == 1
        ht.delete('A')
        assert len(ht) == 0

    def test_contains(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.contains('I') is True
        assert ht.contains('V') is True
        assert ht.contains('X') is True
        assert ht.contains('A') is False
    
    # my test
    def test_contains_after_delete(self):
        ht = HashTable()
        ht.set('A', 1)
        assert ht.contains('A') == True
        ht.delete('A')
        assert ht.contains('A') == False
    
    # my test
    def test_get_after_delete(self):
        ht = HashTable()
        ht.set('A', 10)
        assert ht.get('A') == 10
        ht.delete('A')
        
        with self.assertRaises(KeyError):
            ht.get('A')
    
    # my test
    def test_set_after_delete(self):
        ht = HashTable()
        ht.set('A', 10)
        assert ht.get('A') == 10
        ht.delete('A')
        with self.assertRaises(KeyError):
            ht.get('A')
        ht.set('A', 10)
        assert ht.get('A') == 10

    def test_set_and_get(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.get('I') == 1
        assert ht.get('V') == 5
        assert ht.get('X') == 10
        assert ht.length() == 3
        with self.assertRaises(KeyError):
            ht.get('A')  # Key does not exist

    def test_set_twice_and_get(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 4)
        ht.set('X', 9)
        assert ht.length() == 3
        ht.set('V', 5)  # Update value
        ht.set('X', 10)  # Update value
        assert ht.get('I') == 1
        assert ht.get('V') == 5
        assert ht.get('X') == 10
        assert ht.length() == 3  # Check length is not overcounting
    
    def test_delete_non_existant_items(self):
        ht = HashTable()
        with self.assertRaises(KeyError):
            ht.delete('A')

    def test_delete(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.length() == 3
        ht.delete('I')
        ht.delete('X')
        assert ht.length() == 1
        with self.assertRaises(KeyError):
            ht.delete('X')  # Key no longer exists
        with self.assertRaises(KeyError):
            ht.delete('A')  # Key does not exist


if __name__ == '__main__':
    unittest.main()
