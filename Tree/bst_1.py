
class BinaryTree:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = BinaryTree(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = BinaryTree(val)
                else:
                    self.right.insert(val) 
        else:
            self.val = val
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()
    
root = BinaryTree(100)
root.insert(50)
root.insert(55)
root.insert(10)
root.insert(170)
root.insert(40)
root.insert(130)
root.insert(109)



# root.insert(10)
# root.insert(10)

root.printTree()