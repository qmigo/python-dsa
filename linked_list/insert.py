class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
    
    def insert_at_beg(self,data):
        node = Node (data, self.head)
        self.head = node
    
    def insert_at_end(self,data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = node

    def insert_at_index(self, data, index):
        if index == 0:
            self.head = Node(data, self.head)
            return
        
        index-=1
        itr = self.head

        while index > 0:
            itr = itr.next
            index-=1
        
        itr.next = Node(data, itr.next)

    def insert(self, data_list):
        self.head = None
        for item in data_list:
            self.insert_at_end(item)

    def insert_after_value(self, data, value):   
        itr = self.head
        while itr:
            if itr.data == data:
                itr.next = Node(value, itr.next)
                break
            itr = itr.next

    def insert_before_value(self, data, value):
        fast = self.head
        slow = self.head
        while fast:
            if fast.data == data:

                if fast == self.head:
                    self.insert_at_beg(value)
                    break

                while slow.next != fast:
                    slow = slow.next
                
                slow.next = Node(value, slow.next)
                break
            fast = fast.next

    def put_before(self, data, value): #same as insert before but using single pointer
        itr = self.head
        if self.head.data == data:
            self.insert_at_beg(value)
    
        while itr:
            if itr.next.data == data:
                itr.next = Node(value, itr.next)
                break
            itr = itr.next


    def delete_at_index(self, index):
        if self.head is None:
            print('Empty List')
            return

        if index == 0:
            self.head = self.head.next
            return
        
        index = index-1
        itr = self.head

        while index > 0:
            itr = itr.next
            index-=1

        itr.next = itr.next.next
        print(itr.data)
    
    def remove_first_occurence(self, data):
        fast = self.head
        slow = self.head

        while fast:
            if fast.data == data:

                if fast == self.head:
                    self.head = self.head.next
                    break
                
                while slow.next != fast:
                    slow = slow.next
                
                slow.next = fast.next
                break
            fast = fast.next
    
    def remove_n_occurence(self, data, n=None):
        if n is None:
            n=self.size()

        fast = self.head
        slow = self.head

        while fast and n!=0:
            if fast.data == data:

                if fast == self.head:
                    self.head = self.head.next
                    break
                
                while slow.next != fast:
                    slow = slow.next
                
                slow.next = fast.next
                n-=1
                
            fast = fast.next

    def size(self):
        count = 0
        itr = self.head

        while itr:
            itr = itr.next
            count+=1

        return count

    def reverse_list(self):
        if self.head is None or self.head.next is None:
            return 
        itr = self.head
        while itr:
            future = itr.next

            if itr == self.head:
                itr.next = None
                past = itr
                itr = future
                continue

            if itr.next is None:
                self.head = itr

            itr.next = past
            past = itr
            itr = future

    def reverse_recurse(self, itr):
        if itr.next == None:
            self.head = itr
            return
        self.reverse_recurse(itr.next)
        itr.next.next = itr
        itr.next = None

    def midddle_of_list(self, head):
        if head == None:
            return head
        fast = head
        slow = head

        while fast.next !=None and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def print_list(self):
        if self.head is None:
            print('Empty List')
            return
        
        sll = ''
        itr = self.head

        while itr:
            sll+= str(itr.data) + ' --> '
            itr = itr.next
        
        return sll

    def merge_sorted_list(self, list1, list2):
        if list1 is None:
            return list2

        if list2 is None:
            return list2
        
        if list1.data < list2.data:
            list1.next = self.merge_sorted_list(list1.next, list2)
            return list1
            
        else:
            list2.next = self.merge_sorted_list(list2.next, list1)
            return list2


    def merge_sort(self, head):
        if head == None or head.next == None:
            return head

        middle = self.midddle_of_list(head)
        next_to_middle = middle.next
        
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        list = self.merge_sorted_list(left, right)
        return list

def sorted_list_merge(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.data > list2.data:
        list1, list2 = list2, list1

    head = list1

    while list1.next and list2:
        if list1.next.data > list2.data:
            # print(list2.data)
            future = list2.next
            list2.next = list1.next
            list1.next = list2
            list2 = future
            list1 = list1.next
        
        else:
            # print(list1.data)
            list1 = list1.next

    
    while list1.next:
        list1 = list1.next

    # print(list1.data)
    list1.next = list2  
    return head

def print_list(head):
        if head is None:
            print('Empty List')
            return
        
        sll = ''
        itr = head

        while itr:
            sll+= str(itr.data) + ' --> '
            itr = itr.next
        
        return sll

if __name__ == '__main__':
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert([61, 91])
    ll2.insert([2,4,27,36,42,53,91,95])
    
    print(ll1.print_list())
    print(ll2.print_list())
    print(print_list(sorted_list_merge(ll1.head, ll2.head)))


    