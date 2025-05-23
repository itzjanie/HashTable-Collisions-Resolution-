from hashtable_open_addressing import HashTable

if __name__ == "__main__":
    ht = HashTable(30)
    with open('student_data.csv', 'r') as fhand:
        fhand.readline()
        for line in fhand:
            line = line.strip().split(',')
            id = line[0]
            data = line[1:]
            ht.setitem(id, data)
    print(ht)
    """
    1. Extract the records from the student_data file
    and add them one at a time, as a Python dict, 
    containing the name, class and their associated
    data as key-value dict pairs, to the hashtable
    
    2. You can use the id as the hash table key for 
    each of the above records.
    """
    
    # Test your hashtable using appropriate methods
    # from your implementation
    # ht = HashTable(10)
    # records = {'id': 1234, 'name': 'john'}
    # ht.setitem('id', records)
    # print(ht)
    # print(ht.getitem('ie'))