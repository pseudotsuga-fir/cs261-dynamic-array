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
        self.full()
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
        if self.length == 0:
            raise IndexError("Cannot pop empty list")
        pop = self.data[self.length-1]
        self.data = self.data[0:self.length-1]
        self.length -= 1
        return pop

    def delete(self,index):
        if index < 0 or index > self.length:
            raise IndexError("index out of bounds")
        if self.length == 0:
            raise IndexError("index out of bounds")
        self.data = self.data[self.data!=self.data[index]]
        self.next_index -= 1
        self.length -= 1

    def insert(self,index,num):
        if index < 0 or index > self.length:
            raise IndexError("index out of bounds")
        self.full()
        self.data = np.insert(self.data,index,num)
        self.next_index += 1
        self.length += 1

    def is_full(self):
        if self.length == self.capacity:
            return True
        return False
    
    def full(self):
        if self.is_full():
            self.capacity += 10
            self.data.resize(self.capacity)
            # temp_array = self.data
            # self.data = np.empty(self.capacity, object)
            # self.data = np.concatenate((temp_array,self.data))

    def max(self):
        max_num = self.data[0]
        for item in self.data:
            if item == None:
                pass
            elif item > max_num:
                max_num = item
        return max_num
    
    def min(self):
        min_num = self.data[0]
        for item in self.data:
            if item == None:
                pass
            elif item < min_num:
                min_num = item
        return min_num

    def sum(self):
        array_sum = 0
        for item in self.data:
            if item == None:
                pass
            else:
                array_sum += item
        if array_sum == 0:
            return None
        return array_sum

    def linear_search(self, num):
        for i in range(0,self.length):
            if self.data[i] == num:
                return i
        return None

    def binary_search(self, num):
        return self.binary_search_actually(num,0,len(self.data))
        # low_i = 0
        # mid_i = 0
        # high_i = self.length-1
        # while low_i <= high_i:
        #     mid_i = (high_i + low_i)//2
        #     if self.data[mid_i] > num:
        #         high_i = mid_i - 1
        #     elif self.data[mid_i] < num:
        #         low_i = mid_i - 1
        #     else:
        #         return mid_i
        # return None
    
    def binary_search_actually(self, num, low, high):
        #I couldn't get the non-recursive one to work for the life of me, and python doesn't support function overloading like java does, so I just made another function.
        if low >= high:
            return None
        mid = (low+high)//2
        if num == self.data[mid]:
            return mid
        if num < self.data[mid]:
            return self.binary_search_actually(num, low, mid-1)
        else:
            return self.binary_search_actually(num, mid+1, high)

