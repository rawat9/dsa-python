class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        if self.root == None:
            self.root = node
        else:
            current = self.root
            while True:
                if value < current.value:
                    # left
                    if not current.left:
                        current.left = node
                        return self
                    # otherwise, move futher down
                    current = current.left
                else:
                    # right
                    if not current.right:
                        current.right = node
                        return self
                    current = current.right

    def lookup(self, value):
        comparision = 0
        if not self.root:
            return False

        current = self.root
        while current:
            comparision += 1
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            elif current.value == value:
                return True
        return False

    def remove(self, value):
        if not self.root:
            return False
        current = self.root
        parent = None

        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            elif value == current.value:
                # we have a match

                # Option1 - No right child:
                if current.right == None:
                    if parent == None:
                        self.root = current.left
                    else:
                        # if parent > current then make current.left <- left child of parent
                        if parent.value > current.value:
                            parent.left = current.left

                        # if current > parent then make current.left <- right child of parent
                        elif parent.value < current.value:
                            parent.right = current.left

                # Option2 - Right child that doesn't have left child
                elif current.right.left == None:
                    if parent == None:
                        self.root = current.left
                        return
                    else:
                        current.right.left = current.left

                        # if parent > current then make current.right <- left child of parent
                        if parent.value > current.value:
                            parent.left = current.right

                        # if parent < current then make current.right <- right child of parent
                        elif parent.value < current.value:
                            parent.right = current.right

                # Option3 - Right child that doesn't have right child
                else:
                    # find the right child's left most child
                    leftmost = current.right.left
                    leftmostParent = current.right
                    while leftmost != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    # Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = current.left
                    leftmost.right = current.right

                    if parent == None:
                        self.root = leftmost
                    else:
                        if parent.value > current.value:
                            parent.left = leftmost

                        elif parent.value < current.value:
                            parent.right = leftmost
            return "Not Found"


    def print_tree(self, traversal='inOrder'):
        if traversal == 'preOrder':
            return self.preOrder(self.root, [])
        elif traversal == 'postOrder':
            return self.postOrder(self.root, [])
        else:
            return self.inOrder(self.root, [])

    def preOrder(self, node, result):
        if node:
            result.append(node.value)
            self.preOrder(node.left, result)
            self.preOrder(node.right, result)
        return result
    
    def inOrder(self, node, result):
        if node:
            self.inOrder(node.left, result)
            result.append(node.value)
            self.inOrder(node.right, result)
        return result

    def postOrder(self, node, result):
        if node:
            self.postOrder(node.left, result)
            self.postOrder(node.right, result)
            result.append(node.value)
        return result

    def bfs(self):
        current = self.root
        result = []
        
        # to keep track of the level
        queue = []
        queue.append(current)

        while len(queue) > 0:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

    def bfs_recursive(self, queue, result):
        if len(queue) == 0: 
            return result
        
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        return self.bfs_recursive(queue, result)

    def minHeight(self, node):
        if node == None:
            return -1

        left_height = self.minHeight(node.left)
        right_height = self.minHeight(node.right)

        return 1 + min(left_height, right_height)

    def maxHeight(self, node):
        if node == None:
            return -1

        left_height = self.minHeight(node.left)
        right_height = self.minHeight(node.right)

        return 1 + max(left_height, right_height)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(9)  # root
    bst.insert(4)
    bst.insert(12)
    bst.insert(1)
    bst.insert(6)
    bst.insert(11)
    bst.insert(17)
    bst.insert(0)
    bst.insert(7)
    print(bst.lookup(17))
    """
            9
        4        12
    1      6   11   17 
    """
    bst.print_tree()
    print(bst.minHeight(bst.root))
    print(bst.maxHeight(bst.root))
