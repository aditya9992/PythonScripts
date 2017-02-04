# Program for Binary Tree traversal

class BinaryTree: 
    def __init__(self,initdata):
        self.data = initdata
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def preorder(self, node):
        if node:    
            print(node.getData())
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.getData())
            self.inorder(node.right)
    
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.getData())
    
    def height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def levelorder(self, node):
        h = self.height(node)
        for i in range(1, h + 1):
            self.levelprint(node, i)

    def levelprint(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.getData())
        elif level > 1:
            self.levelprint(node.left, level - 1)
            self.levelprint(node.right, level -1)

    def levelorder_queue(self, node):
        if node is None:
            return
        
        queue = []

        queue.append(node)
        while(len(queue) > 0):
            print(queue[0].data)

            n = queue.pop(0)

            if n.left is not None:
                queue.append(n.left)
            if n.right is not None:
                queue.append(n.right)