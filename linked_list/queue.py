class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next =None

class Que:
    def __init__(self, front=None, rear=None) -> None:
        self.front = front
        self.rear = rear

    def append(self,data):
        node = Node(data)
        
        if self.front is None:
            self.front = node
            self.rear = node

        self.rear.next = node
        self.rear = node
        
    
    def print_list(self):
        if self.rear is None:
            print('Queue Empty')
            return
        
        sq = ''
        itr = self.front
        while itr:
            sq+= str(itr.data) + ' -> '
            itr = itr.next
        
        return sq

    def pop_back(self):
        pass

    
if __name__ == '__main__':
    queue = Que()
    queue.append(2)
    queue.append(2)
    queue.append(12)
    queue.append(22)

    sq = queue.print_list()
    print(sq)
