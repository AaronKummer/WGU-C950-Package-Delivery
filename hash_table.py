class HashTable(object):
     
    def __init__(self,size):
         
        # We set up size and slots and data
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
         
    def put(self,key,data):
         
        # We get the hash value
        hashvalue = self.hashfunction(key,len(self.slots))
 
        # in case Slot is Empty
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
         
        else:
             
            # If the key already exists, replace old value
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  
             
            # Otherwise, find the next available slot - collision case
            else:
                 
                nextslot = self.rehash(hashvalue,len(self.slots))
                 
                # Get to the next slot
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                 
                # Set new key, if NONE
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                     
                # Otherwise replace old value
                else:
                    self.data[nextslot] = data 
 
    def hashfunction(self,key,size):
        # Remainder Method
        return key%size
 
    def rehash(self,oldhash,size):
        # For finding next possible positions
        return (oldhash+1)%size
     
     
    def get(self,key):
         
        # Get the  items given a key
         
        # Set up variables for our search
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
         
        # Until we discern that its not empty or found (and haven't stopped yet)
        while self.slots[position] != None and not found and not stop:
             
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                 
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                     
                    stop = True
        return data
 
    # Special Methods for use with Python indexing
    def __getitem__(self,key):
        return self.get(key)
 
    def __setitem__(self,key,data):
        self.put(key,data)