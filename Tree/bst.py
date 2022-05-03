class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self, key) -> None:
        self.root = Node(key)
    
    def insert(self, root, key):
        if root.data < key:
            if root.right is None:
                root.right = Node(key)
                print('success',root.right.data)
            else:
                root.right = self.insert(root.right, key)

        else:
            if root.left is None:
                root.left = Node(key)
                print('success',root.left.data)

            else:
                root.left = self.insert(root.left, key)
    
    def preorder(self,root):
        if root:
            self.preorder(root.left)
            print(root.data)
            self.preorder(root.right)

if __name__ == '__main__':
    bst = BST(5)
    r = bst.root
    
    bst.insert(r, 6)
    bst.insert(r, 7)
    bst.insert(r, 1)
   
    print(r.right)
    
