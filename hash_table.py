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

    def hash(self, key) -> int:
        return hash(key) % self.size 


H = HashTable()
H.set('a', "2530")
H.set(3, "233 Canyon Rd,Salt Lake City,UT,84103,EOD,2,Can only be on truck 2")

print(H.map)