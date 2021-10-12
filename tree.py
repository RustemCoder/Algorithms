class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

node  = Node(10)
node.left = Node(5)
node.right = Node(15)
node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

print(node.right.data)
print(node.right.right.data)
myTree = node.left
class Tree:
    def __init__(self,root,name=''):
        self.root = root
        self.name = name
myTree = Tree(node,'Rustem\'s tree')
print(myTree.name)
print(myTree.root.right.right.data)
print(myTree.root.left.left)