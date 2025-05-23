class HashTable:
    def __init__(self, size):
        self.size = size
        self.values = [None] * self.size

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key: str) -> int:
        """Computes and returns the initial location for a given key using built-in hash function"""
        return hash(key) % self.size
      
    def _rehash(self, old_location: int) -> int:
        """
        computes and returns the new location for linear probing
        """
        return (old_location+1) % self.size
    
    def setitem(self, key: str, value: dict) -> None:
        """
        adds or updates a key-value pair in the list and raises an exception if the table is full
        """
        location = self._hash(key)
        old_location = location
        if self.values[location] == None:
            self.values[location] = [key, value]
        elif self.values[location][0] == key:
            self.values[location] = [key, value]
        else:
            while self.values[location] != None:
                if self.values[location][0] != key:
                    location = self._rehash(location)
                elif location == old_location:
                    print('The hashtable is full. Please try again.')
                    return False
            self.values[location] = [key, value]
            
    

    def getitem(self, key: str) -> 'dict | None':
        """
        return the value of the associated with the key and raise a Keyerror if the key is not found
        """
        location = self._hash(key)
        old_location = location
        if self.values[location] == None:
            raise KeyError
        elif self.values[location][0] == key:
            return self.values[location][1]
        else:
            while self.values[location][0] != key:
                location = self._rehash(location)
                if location == old_location:
                    raise KeyError
            return self.values[location][1]    
            
