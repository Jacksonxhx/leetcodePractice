class RandomizedSet:

    def __init__(self):
        self.res = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.res.append(val)
            self.pos[val] = len(self.res) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            idx, last = self.pos[val], self.res[-1]
            self.res[idx] = last
            self.pos[last] = idx
            self.res.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        return self.res[random.randint(0, len(self.res) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()