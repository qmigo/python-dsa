class BinaryTree:
    def __init__(self,name, val,parent=None) -> None:
        self.val = val
        self.name = name
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, name, key):
        if key < self.val:
            if self.left is None:
                self.left = BinaryTree(name, key, self)
            else:
                self.left.insert(name, key)
        else:
            if self.right is None:
                self.right = BinaryTree(name,key,self)
            else:
                self.right.insert(name, key)
    
    def search(self, key):

        if key == self.val:
            return True

        if key < self.val:
            if self.left is None:
                return False
            return self.left.search(key)
        else:
            if self.right is None:
                return False
            return self.right.search(key)
         

    def preorder(self):
        
        if self.parent is None:
            print(self.val,'->',None)

        if self.parent :
            parents = list()
            temp = self.parent
            
            while temp :
                parents.append(temp.val)
                temp=temp.parent
            

            print('  '*len(parents), '|_',self.val,'->',parents)

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def bfs(self):
        if self is None:
            return
        if self:
            queue = [self]
        
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur.parent is None:
                print(cur.name,'->',None)

            if cur.parent :
                parents = list()
                temp = cur.parent
            
                while temp :
                    parents.append(temp.name)
                    temp=temp.parent
            

                print('  '*len(parents), '|_',cur.name,'->',parents)
        
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

root = BinaryTree('Ankur',20)
root.insert('Ankit',24)
root.insert('Madhav',21)
root.insert('Randheer',22)
root.insert('Radha',23)
root.insert('Keshav',19)
# root.insert(160)
# root.insert(130)
# print(root.parent)
root.bfs()
root.preorder()
# if root.search(10) is True:
#     print('found')
# else:
#     print('not found')
