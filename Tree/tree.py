class BST:
    def __init__(self, val, parent=None) -> None:
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
    
    def insert(self, key):
        if key < self.val:
            if self.left is None:
                self.left = BST(key, self)
            else:
                self.left.insert(key)
        elif key > self.val:
            if self.right is None:
                self.right = BST(key, self)
            else :
                self.right.insert(key)

    def smallest(node):
        while node.left:
            node = node.left
        return node

    def remove(self, key):
        if self is None:
            return self
        
        if key < self.val:
            self.left = self.left.remove(key)
        
        elif key > self.val:
            self.right = self.right.remove(key)
        
        else:
            
            if self.left is None:
                temp = self.right
                self = None
                return temp
            
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = self.right.smallest()
            self.val = temp.val
            self.right = self.right.remove(temp.val)
        return self



    def inorder(self):
        if self.parent:
            temp = self.parent
            count=0
            while temp:
                temp= temp.parent
                count+=1
            print(' '*count,'|__',self.val)
        else:    
            print(self.val)

        if self.left:
            self.left.inorder()

        if self.right:
            self.right.inorder()

    def bfs(self):
        if self is None :
            return self
        queue = [self]
        while len(queue)>0:
            cur = queue.pop(0)

            if cur.parent:
                temp = cur.parent
                count=0
                while temp:
                    temp= temp.parent
                    count+=1
                print('  '*count,'|__',cur.val)
            else:    
                print(cur.val)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    
    def trimBST(self,l ,r):
        if self is None :
            return None

        if self.val < l:
            self.left = None
            return self.right
        elif self.val > r:
            self.right = None
            return self.left

        else:
            if self.left:
                self.left = self.left.trimBST(l,r)
            if self.right:
                self.right = self.right.trimBST(l,r)

        return self

    def mirror(self):
        if self is None:
            return

        if self.left:
            self.left.mirror()

        if self.right:
            self.right.mirror()

        temp = self.left
        self.left = self.right
        self.right = temp 

    
if __name__ == '__main__':
    root = BST(5)
    root.insert(2)
    root.insert(8)
    root.insert(1)
    root.insert(4)
    root.insert(6)
    root.insert(9)

    root.bfs()
    root.mirror()
    root.bfs()

    
