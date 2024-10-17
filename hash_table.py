# Name:  - Zoe Buck <br>
# References:  - https://en.wikipedia.org/wiki/Rolling_hash, https://www.geeksforgeeks.org/python-bitwise-operators/, https://computinglife.wordpress.com/2008/11/20/why-do-hash-functions-use-prime-numbers/ <br>

import time
import csv          # Used to read a .csv file.


def new_array(size: int):
    
    """ Creates a new array of a given size.
    :param size: (int) the number of 0s you want in the array
    :return : (list) the array with zeros 
    >>> new_array(3)
    [0,0,0]
    """
    L = [0] * size
    return L

class HashNode:
    """Class to instantiate linked list node objects, with both a key and a value.
    >>> node = HashNode(7, "Matt Damon")
    >>> print(node)
    {key:7, value:Matt Damon}
    """
    
    def __init__(self, key:int, value:str) -> object:
        """ Constructor of new node with a key and value. Initially nodes do not have a next value.
        :param key: (int) the key that will be added to the node
        :param value: (str) the value that will be added to the node
        :return : (HashNode) a pointer to the object
        """
        self.key = key
        self.value = value
        self.next = None
       
    def __str__(self) -> str:
        """ Returns a string representation of the object.
        :return : (str) a string description of the HashNode object.
        """
        return "{key:" + str(self.key) + ", value:" + self.value + "}"     




class linkedList:
    """A class representing a singly linked list of HashNode objects
    >>> myList = LinkedList()
    >>> myList.add(194, "hello")
    >>> myList.add(69, "goodbye")
    >>> printLL(myList)
    {key:194, value:hello}, {key:69, value:goodbye},
    
    """
    #initialize
    def __init__(self) -> object:
        """ Constructor of a linked list. Initially the head (first node in the list) has no value.
        :return : (linkedList) a pointer to the object
        """
        self.head = None

    def add(self, key:int, data:str):
        """ Inserts new node containing given data at the start of the linked list. If the list has no head, the new node will become the head
        :param key: (int) The key that will be stored in the newly created node in the linkedList.
        :param data: (string) data to be stored in a new node in the linkedList

        >>> ll = linkedList()
        >>> ll.add(1, "john")
        >>> str(ll.head)
        {key:1, value:john},
        """
        myNode = HashNode(key, data)
        if self.head is None:
            self.head = myNode
            #return
        else:
            myNode.next = self.head
            self.head = myNode

    
    def remove(self, key):
        """ Removes the node containing the given key in the linkedList. If there are duplices only the first node with the key will be removed.

        :param key: (int) The key inside the node to be removed
        :return: (bool) True if the node was successfully removed, False otherwise.

        >>> ll = linkedList()
        >>> ll.add(1, "john")
        >>> ll.remove(1)
        True
        >>> ll.remove(2)
        False
        """
        if self.head == None:
            #raise Exception("The linked list is empty")
            return False
        if self.head.key == key:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next != None and current_node.next.key != key:
                current_node = current_node.next
            if current_node.next == None:
                #raise Exception("That data is not in the Linked List")
                return False
            else:
                current_node.next = current_node.next.next
        return True

    def contains(self, key:int):
        """Checks whether the linked list contains a node with the specified key.
        
        :param key: (int) The key to search for.
        :return: (bool) True if the key exists, False otherwise.
        
        >>> ll = linkedList()
        >>> ll.add(1, "john")
        >>> ll.contains(1)
        True
        >>> ll.contains(2)
        False
        """
        current_node = self.head
        while current_node != None:
            if current_node.key == key:
                return True
            current_node = current_node.next
        return False
    
    
    def printLL(self):
        """Prints all the key-value pairs in the linked list.
        
        >>> ll = linkedList()
        >>> ll.add(1, "john")
        >>> ll.add(2, "bob")
        >>> ll.printLL()
        {key: 2, value: john }, {key: 1, value: bob },
        """
        current_node = self.head
        while(current_node):
            print("{key: ", str(current_node.key), ", value: ", current_node.value, "},", end = ' ')
            current_node = current_node.next
        


class HashTable:
    """A class representing a hash table data structure.
    
    >>> ht = HashTable(10, 1)
    >>> ht.insert(12, 'john')
    >>> ht.insert(5, 'bob')
    >>> print(ht)
    At index 0: {key: 5, value: 'bob' }, {key: 12, value: 'john'},
    """
    
    #constructs a new empty hash table
    def __init__(self, size:int, hash_choice:int) -> object:
        """Initializes a hash table with a specified size and hash function.
        
        :param size: (int) The number of slots in the hash table.
        :param hash_choice: (int) The hash function choice (0-4). Corresponds with different hash functions.
        
        >>> ht = HashTable(10, 0)
        >>> ht.size
        10
        >>> ht.hash_choice
        0
        """
        self.size = size
        self.hash_choice = hash_choice      # Which hash function you will use.              
        self.table = [None] * size          
        self.occupied = 0                   #number of key/value pairs added to the hashtable
        ###bucket = size
        pass
    
    # returns a human readable version of the contents of the hash table 
    def __str__(self) -> str:
        """Prints a human-readable version of the hash table's contents.
        
        :return: (str) A string reading "Hash Table"
        
        >>> ht = HashTable(10, 0)
        >>> print(ht)
        Hash Table
        >>> ht.insert(125, "john")
        >>> print(ht)
        At index 5: {key: 125, value: "john" }
        """
        index = 0
        while index < self.size:
            if self.table[index] and self.table[index].head:
                print("At index ", index, ": ")
                self.table[index].printLL()
                print("\n")
            index += 1
        return "Hash Table"

    def hash_polynomial(self, key: int, a: int = 31) -> int:
        """A polynomial rolling hash function.
        
        :param key: (int) The key to hash.
        :param a: (int) The base constant, default is 31.
        :return: (int) The hash value.

        >>> self.size = 10
        >>> hash_polynomial(125) 
        8
        """
        hash_value = 0
        key_str = str(key)  # Treat the integer as a string of digits
        for digit in key_str: # Iterate over each digit
            hash_value = (hash_value * a + int(digit)) % self.size
        return hash_value


    def hash_bit_move(self, key: int, prime: int = 31) -> int:
        """A hash function that multiplies the given key by a prime number and shifts the result 5 bits right. Reference: https://www.geeksforgeeks.org/python-bitwise-operators/
        
        :param key: (int) The key to hash.
        :param prime: (int) A base constant, default is 31. Ideally a prime number for more even distribution.
        :return: (int) The hash value.
        
        >>> self.size = 10
        >>> hash_mul_shift(4, 17)
        5
        """

        return (((key * prime) >> 5) % self.size)



    
    def hashFunc(self, key:int) -> int:
        """Computes the hash value of a key based on the hash function corresponding with a given integer. Treated as a private function.
        
        :param key: (int) The key to hash.
        :return: (int) The hash value of the key, or None if the key given is not an int.
        
        >>> ht = HashTable(10, 1)
        >>> ht.hashFunc(5)
        0
        """
        if type(key) != int:
            return None
        if self.hash_choice == 0:
            return hash(key) % self.size    #Embedded Python hash function.
        elif self.hash_choice == 1:
            return 0    #Everything in the has ia stored in a single linked list.
        elif self.hash_choice == 2:
            constant = 991 #constant that should be a prime for more even distribution 
            return key * constant % self.size  # Multiple by the constant mod size
        elif self.hash_choice == 3:
            return self.hash_bit_move(key, 991) 
        elif self.hash_choice == 4:
            return self.hash_polynomial(key, 991)
        return None
    

    def insert(self, key:int, val:str) -> bool:
        """Inserts a key-value pair into the hash table.
        
        :param key: (int) The key to insert.
        :param val: (str) The value to associate with the key.
        :return: (bool) True if the insertion was successful, False if the key already exists in the table.
        
        >>> ht = HashTable(10, 0)
        >>> ht.insert(1, "john")
        True
        >>> ht.insert(1, "bob")
        False
        """
        index = self.hashFunc(key)
        if self.table[index] is None: #nothing has been added to that index yet
            newList = linkedList() 
            newList.add(key, val) 
            self.table[index] = newList #should i put the linked list or node here? 
        else: #There is already a linkedlist
            if self.table[index].contains(key): #check if that key is already in the linked list
                return False #Already in linked list!
            self.table[index].add(key, val)
        self.occupied += 1
        return True


    def getValue(self, key:int) -> str:
        """Retrieves the value associated with the specified key.
        
        :param key: (int) The key to search for.
        :return: (str) The value associated with the key, or None if the key does not exist.
        
        >>> ht = HashTable(10, 0)
        >>> ht.insert(1, "john")
        True
        >>> ht.getValue(1)
        'john'
        >>> ht.getValue(2)
        None
        """
        index = self.hashFunc(key)
        if self.table[index] == 0:
            return None
        current_node = self.table[index].head
        while current_node != None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        return None


    def remove(self, key:int) -> bool:
        """Removes a key-value pair from the hash table.
        
        :param key: (int) The key to remove.
        :return: (bool) True if the key was successfully removed, False otherwise.
        
        >>> ht = HashTable(10, 0)
        >>> ht.insert(1, "john")
        True
        >>> ht.remove(1)
        True
        >>> ht.remove(2)
        False
        """
        index = self.hashFunc(key)
        if self.table[index] == None: #the key is not in the hashtable because there is nothing at the expected index
            return False
        self.occupied -=1
        return self.table[index].remove(key)
    
    #calculates the load factor for the current table and returns True if and only if it is greater 
    # than 0.7
    def isOverLoadFactor(self) -> bool:
        """Checks if the hash table's load factor exceeds 0.7. The load factor is defined as the number of items stored in the table (represented by self.occupied) divided by the size of the table
        
        :return: (bool) True if the load factor is above 0.7, False otherwise.
        
        >>> ht = HashTable(10, 0)
        >>> i = 0
        >>> while i < 10:
        >>>     ht.insert(i, 'john')
        >>>     i+=1
        >>> ht.isOverLoadFactor()
        True
        """
        if self.occupied/self.size > 0.7:
            return True
        return False

    
    def reHash(self) -> bool: 
        """Creates a new hash table that is double the size of the current one and rehashes all of the key, value pairs into the new table if the load factor exceeds 0.7.
        
        :return: (bool) True if rehashing was successful, False if the load factor is smaller than 0.7.
        
        >>> ht = HashTable(10, 0)
        >>> ht.occupied = 8
        >>> ht.reHash()
        True
        """
        if not self.isOverLoadFactor(): #not over load factor yet, and should not rehash
            return False 
        oldSize = self.size
        oldHashTable = self.table

        self.size = self.size * 2
        self.table = [None] * (self.size) 
        self.occupied = 0

        index = 0
        while index < oldSize:
            if oldHashTable[index]:
                current_node = oldHashTable[index].head
                while current_node:
                    self.insert(current_node.key, current_node.value)  
                    current_node = current_node.next
            index +=1
        return True
            
                    
def main():
    """Main function to test hash table functionality via user input."""

    # Can play around with these three values 
    hash_to_test = 3    
    initial_bucket_size = 5 
    initial_num_to_add = 5

    hash_table = HashTable(initial_bucket_size, hash_to_test)
    with open('people_data.csv') as csv_file:    
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = csv_reader.__next__()
        for row_iterator in range(initial_num_to_add):
            row = csv_reader.__next__()
            hash_table.insert(int(row[0]),row[1])
        print("Hash Map Initialized")
                
        option = ""
        while option != "QUIT":
            option = input("Select an option (ADD, GET, REMOVE, PRINT, CHECK, REHASH, QUIT): ").upper()        

            if option == "ADD":
                row = csv_reader.__next__()
                hash_table.insert(int(row[0]),row[1])
                print("Added - Key:", int(row[0]), "\tValue:", row[1])
            elif option == "GET":
                key = int(input("Which # would you like to get the value of? "))
                val = hash_table.getValue(key)
                if val is None:
                    print("Error,", key, "not found.")
                else:
                    print(val)
            elif option == "REMOVE":
                key = int(input("Which # would you like to remove? "))
                suc = hash_table.remove(key)
                if suc:
                    print(key, "was removed.")
                else:
                    print("Error,", key, "was not removed.")                    
            elif option == "PRINT":
                print(hash_table)   # calls the __str__ method.  
            elif option == "CHECK":
                isOver = hash_table.isOverLoadFactor()
                if isOver:
                    print("Your load factor is over 0.7, it's time to rehash.")
                else:
                    print("Load factor is ok.")
            elif option == "REHASH":
                suc = hash_table.reHash()
                if suc:
                    print("Rehash was successful.")
                else:
                    print("ERROR: rehash failed.")
            elif option == "QUIT" or option == "Q":
                break 
            else:
                print("Error: invalid input, please try again.")
                
        print("Goodbye!")
            


def profilerMain():    
    """ Function to test speed of main hash table functionality with different hash functions. Saves times to hash_speeds.csv"""
    
    # Update these three values to test their impact on performance of various hash functions
    num_hash_implemented = 5    
    initial_bucket_size = 100 
    initial_num_to_add = 100

    # Save speeds for insert remove, and rehash into csv file hash_speeds.csv for each hash function
    csv_file_path = 'hash_speeds.csv'
    hash_func_descriptions = ["mod size", "always 0", "prime multiplication", "multiplied and bitwise move", "polynomial hash"]

    with open('hash_speeds.csv', 'w', newline='') as file: 
        writer = csv.writer(file)
        field = ["Hash Function", "Load Factor", "Insert", "Remove", "Rehash"]
        writer.writerow(field)

        key_to_delete = None
        for i in range(0, num_hash_implemented):        
            hash_table = HashTable(initial_bucket_size, i)
            # print(hash_table)
            # key_to_delete = int(input("Choose a key to test the time of remove operation on: "))

            
            with open('people_data.csv') as csv_file:    
                csv_reader = csv.reader(csv_file, delimiter=',')
                header = csv_reader.__next__()
                for row_iterator in range(initial_num_to_add):
                    row = csv_reader.__next__()
                    hash_table.insert(int(row[0]),row[1])
                print("Hash Map", i, "Initialized")
                print(hash_table)
                if not key_to_delete:
                    key_to_delete = int(input("Choose a key to test the time of remove operation on: "))

                current_row = new_array(6)
                current_row[0] = str(i) #save current hash function number as first column in row
                current_row[1] = hash_table.occupied/hash_table.size #save load factor as second column in row

                # Inserting value into hash
                start_time_create = time.time()    # Get start Time.
                row = csv_reader.__next__() 
                hash_table.insert(int(row[0]),row[1])
                end_time_create = time.time()      # Get end Time.   
                current_row[2] = end_time_create - start_time_create

                # Removing value from the hash
                start_time_create = time.time() 
                hash_table.remove(key_to_delete)
                end_time_create = time.time()
                current_row[3] = end_time_create - start_time_create

                # Rehashing the hash
                start_time_create = time.time() 
                suc = hash_table.reHash()
                end_time_create = time.time()
                current_row[4] = end_time_create - start_time_create
        

                current_row[5] = hash_func_descriptions[i]
            
                writer.writerow(current_row) #write row to csv file
        
    

if __name__ == "__main__":
    # Swap these options to profile or test code
    profilerMain()     
    #main()
    
