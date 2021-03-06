from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ : Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    # Creates an array
    arr = []
    # Makes various linked list objects and appends them to the array
    for i in range(size):
      new_list = LinkedList()
      arr.append(new_list)

    return arr




  # 2️⃣ : Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value 
  # that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    
    length = len(key)
    
    index = length % self.size
    
    return index




  # 3️⃣ : Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a 
  # counter for the number of times the word appeared. When inserting a new word in the hash table, 
  # be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value=1):
   # find the ll @ index --> check if empty, if yes, append
    index = self.hash_func(key)
    ll = self.arr[index]
    
    current = ll.head
    # if not, check if key == key we want to append
    while current != None:
      # if yes, increase value by 1
      if current.data[0] == key:
        current.data[1] += value
        return
      
      current = current.next

    # This means the data was never found (it was empty and thus appending occurs now)
    ll.append([key, value])


  # 4️⃣ : Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    #loop through all the linked lists in the array
    for ll in self.arr:
      current = ll.head
      # if the head of the linked list has information (is not None), print the first and second index
      # of said information (key, value)
      while current != None:
        if current.data:
          print(f'{current.data[0]}: {current.data[1]}')
        # move on to the next node in the linked list

        current = current.next



