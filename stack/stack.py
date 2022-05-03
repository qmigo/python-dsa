from operator import le
from typing import DefaultDict

#this has to be added

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class FreqStack:
    def __init__(self) -> None:
        self.head = None
    
    def push(self,val):
        node = Node(val,self.head)
        self.head = node
    

    def find_ele(self):
        itr = self.head
        freq = {}
        count = 1
        while itr:
            freq.setdefault(str(itr.val), []).append(count)
            itr = itr.next
            count+=1
        # print(freq)
        max_len=-1
        for key in freq:
            if len(freq[key]) > max_len:
                max_len=len(freq[key])
        min_len = int(100000)
        val =-1
        for key in freq:
            if len(freq[key]) == max_len:
                # print(freq[key][0])
                if freq[key][0] < min_len:
                    min_len = freq[key][0]
                    val = key
        # print('#',max_len,val)
        print(val)
        return val
                



    def pop(self):
        val = self.find_ele()
        # print(val)
        # val = self.head.val
        slow = self.head
        fast = self.head
        while fast:
            if int(fast.val) == int(val):
                break
            fast = fast.next
        
        
        if fast == self.head:
            self.head = self.head.next
            # print(val)
            return val
            
        while slow.next != fast:
            slow = slow.next
        slow.next = fast.next

        # print(val)
        return val
        
    def show(self):
        itr = self.head
        while itr:
            print(itr.val,end=' ')
            itr = itr.next
        print()

if __name__ == '__main__':
    freqstack = FreqStack()
    freqstack.push(1)
    freqstack.push(0)
    freqstack.push(0)
    freqstack.push(1)
    freqstack.push(5)
    freqstack.push(4)
    freqstack.push(1)
    freqstack.push(5)
    freqstack.push(1)
    freqstack.push(6)

    # freqstack.show()
    
    freqstack.pop()
    freqstack.pop()
    freqstack.pop()
    freqstack.pop()
    freqstack.pop()
    freqstack.pop()
    freqstack.pop()
    freqstack.pop()
    freqstack.pop()
    freqstack.pop()
    # freqstack.pop()
    
    freqstack.show()

