class HashTable:

    def __init__(self) -> None:
        self.size = 10
        self.map = [None] * self.size

    def get(self,k):
        key = self.hash(k)
        slot = self.map[key]
        for kv in slot:
            k,v = kv
            if key == k:
                return v

    def set(self, key, value):
        key_hash = self.hash(key)

        if self.map[key_hash] == None:
            self.map[key_hash] = list([[key,value]])
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = [key,value]
                    return
            self.map[key_hash].append([key,value])

    def hash(self, key) -> int:
        return hash(key) % self.size 
