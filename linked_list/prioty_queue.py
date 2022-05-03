class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class PriortyQueue:
    def __init__(self, k: int, nums :list[int]) -> None:
        self.head = None
        self.k = k-1
        nums.sort()
        for i in nums:
            self.head = Node(i,self.head)

    def add(self, val):
        if self.head is None:
            self.head = Node(val,self.head)
            return self.head.data

        if val>self.head.data:
            self.head = Node(val,self.head)
            return self.remove()
        
        itr = self.head
        while itr.next and val<itr.next.data:
            itr = itr.next
        itr.next = Node(val,itr.next)
        return self.remove()
        
    
    def remove(self):
        headref = Node()
        headref.next = self.head
        try:
            itr = headref
            k = self.k
            while k>0:
                itr = itr.next
                k-=1
            ans = itr.next.data
            # itr.next = itr.next.next
            self.head = headref.next
            return ans

        except:
            return None
        

    def show(self):
        itr = self.head
        while itr:
            print(itr.data, end=' ')
            itr = itr.next
        
if __name__ == '__main__':
    pq = PriortyQueue(3,[4,5,8,2])
    pq.add(3)
    pq.add(5)
    pq.add(10)
    pq.add(9)
    pq.add(4)
    print()
    pq.show()