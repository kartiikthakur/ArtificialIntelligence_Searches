from sys import maxsize

class BinaryTree():

    def __init__(self, rootid, value):
      self.left = None
      self.right = None
      self.rootid = rootid
      self.value = value

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, value):
        self.value = value

    def getNodeValue(self):
        return self.value

    def insertRight(self, x, newNode):
        if self.right == None:
            self.right = BinaryTree(x, newNode)
        else:
            tree = BinaryTree(x, newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self, x, newNode):
        if self.left == None:
            self.left = BinaryTree(x, newNode)
        else:
            tree = BinaryTree(x, newNode)
            tree.left = self.left
            self.left = tree

def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild())
        print(tree.getNodeValue())
        printTree(tree.getRightChild())

maxi = maxsize
mini = -maxsize - 1
def testTree():
    myTree = BinaryTree("1_00",maxi)
    myTree.insertLeft("1_10",mini)
    myTree.insertRight("1_11",mini)
    l10 = myTree.getLeftChild()
    l10.insertLeft("1_20",maxi)
    l10.insertRight("1_21",maxi)
    l11 = myTree.getRightChild()
    l11.insertLeft("1_22",maxi)
    l11.insertRight("1_23",maxi)

    l20 = l10.getLeftChild()
    l20.insertLeft("1_30",mini)
    l20.insertRight("1_31",mini)
    l21 = l10.getRightChild()
    l21.insertLeft("1_32",mini)
    l21.insertRight("1_33",mini)
    l22 = l11.getLeftChild()
    l22.insertLeft("1_34",mini)
    l22.insertRight("1_35",mini)
    l23 = l11.getRightChild()
    l23.insertLeft("1_36",mini)
    l23.insertRight("1_37",mini)

    l30 = l20.getLeftChild()
    l30.insertLeft("1_40",3)
    l30.insertRight("1_41",10)
    l31 = l20.getRightChild()
    l31.insertLeft("1_42",2)
    l31.insertRight("1_43",9)

    l32 = l21.getLeftChild()
    l32.insertLeft("1_44",10)
    l32.insertRight("1_45",7)
    l33 = l21.getRightChild()
    l33.insertLeft("1_46",5)
    l33.insertRight("1_47",9)

    l34 = l22.getLeftChild()
    l34.insertLeft("1_48",2)
    l34.insertRight("1_49",5)
    l35 = l22.getRightChild()
    l35.insertLeft("1_410",6)
    l35.insertRight("1_411",4)

    l36 = l23.getLeftChild()
    l36.insertLeft("1_412",2)
    l36.insertRight("1_413",7)
    l37 = l23.getRightChild()
    l37.insertLeft("1_414",9)
    l37.insertRight("1_415",1)

    return myTree

tree = testTree()
output = []

def path(root, k, l=[]):
    levels = 5
    if not root:
        return []
    if root.getNodeValue() == k:
        l.append(root.rootid)
        return l

    # Pre-order traversal: Visit root, then left, then right.
    l.append(root.rootid)
    path(root.left, k, l)
    path(root.right, k, l)
    return l[:levels]

def max_value(node):

    if node.getNodeValue() != maxi and node.getNodeValue() != mini:
        return node.getNodeValue()

    children = [node.getRightChild(), node.getLeftChild()]

    for roots in children:
        minimum = min_value(roots)
        maxima = max(mini, minimum)


    return maxima


def min_value(node):
    if node.getNodeValue() != maxi and node.getNodeValue() != mini:
        return node.getNodeValue()

    children = [node.getRightChild(), node.getLeftChild()]
    for roots in children:
        maximum = max_value(roots)
        minima = min(maxi, maximum)


    return minima


def minimax(BTree):
    winner = max_value(BTree)
    return winner

winner = minimax(tree)
print("The Optimal value of the MiniMax Algorithm : "+ str(winner))
print("\n The output Path is :")
print(path(tree,winner))

