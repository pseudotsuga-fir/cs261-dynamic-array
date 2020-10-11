# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Andrew Hepworth
import numpy as np
class DynamicArray:
    pass
    def __init__(self):
        self.capacity = 10
        self.length = 0
        self.next_index = 0
        self.data = np.empty(self.capacity, object)
    
    def __len__(self):
        return self.length

    def is_empty(self):
        if self.length == 0:
            return True
        return False
    
    def append(self,num):
        self.data[self.next_index] = num
        self.next_index += 1
        self.length += 1

    def __getitem__(self, index):
        if index < 0 or index > self.length - 1:
            raise IndexError("index out of bounds")
        return self.data[index]

    def clear(self):
        self.data = np.empty(self.capacity, object)
        self.length = 0
        self.next_index = 0

    def pop(self):
        pop = self.data[self.length-1]
        self.data = self.data[0:self.length-1]
        self.length -= 1
        return pop