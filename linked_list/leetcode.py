
class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
    
    def insert(self,val):
        self.head = Node(val,self.head)



    def print_list(self):
        if self.head is None :
            print('Empty')
        itr = self.head 
        co = 14
        while itr and co>0:
            print(itr.val,end=' , ')
            itr = itr.next
            co-=1
            
    def swapNodes(self,k):
        headref = Node()
        headref.next = self.head

        slow = headref
        fast = headref
        temp = k-1
        
        while temp>0:
            fast = fast.next
            temp-=1

        temp1 = fast.next
        while temp1.next:
            slow = slow.next
            temp1 = temp1.next

        slow_next = slow.next
        fast_next = fast.next

        fast.next = fast_next.next
        slow.next = slow_next.next

        slow_next.next = fast.next
        fast.next = slow_next

        fast_next.next = slow.next
        slow.next = fast_next

        self.head = headref.next
        

if __name__ == '__main__':
    ll = LinkedList()
    lis = [1,2,3,4,5,6,7,8,9]
    for i in lis:
        ll.insert(i)

    ll.print_list()
    
    ll.swapNodes(3)
    # ll.swapNodes(2)
    # ll.swapNodes(1)
    ll.print_list()
