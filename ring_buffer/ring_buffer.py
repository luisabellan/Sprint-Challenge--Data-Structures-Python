class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.age = 0
        self.list = []

    def get(self):
        return self.list

    def append(self, item):
        size = len(self.list)
        capacity = self.capacity

        if size < capacity:
            return self.list.append(item)
        if size >= capacity:
            if self.age == self.capacity:
                self.age = 0
                self.list.insert(self.age, item)
                self.list.pop(self.age+1)
                self.age += 1
            else:
                self.list.insert(self.age, item)
                self.list.pop(self.age+1)
                self.age += 1


'''buffer = RingBuffer(5)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i') 

buffer.get()   # should return ['d', 'e', 'f']'''
