class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree
    
    def insert_right(self,value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def breadth_first_search(self, n):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return False
    
    def preorder_traversal(tree):
        if tree:
            print(tree.key)
            preorder_traversal(tree.left_child)
            preorder_traversal(tree.right_child)
    
    def postorder_traversal(tree):
        if tree:
            postorder_traversal(tree.left_child)
            postorder_traversal(tree.right_child)
            print(tree.key)

    def inorder_traversal(tree):
        if tree:
            inorder_traversal(tree.left_child)
            print(tree.key)
            inorder_traversal(tree.right_child)