class HashTable:

    def __init__(self) -> None:
        self.size = 10
        self.map = [None] * self.size

    # O(n)
    def get(self, key):
        key_hash = self.hash(key)
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # O(n)
    def insert(self, key, value):
        key_hash = self.hash(key)
        key_value = [key, value]

        if self.map[key_hash] == None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # O(1)
    def hash(self, key) -> int:
        return int(key) % self.size 
