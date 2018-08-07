#Create a binary tree

#更改单行输出
class node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

#前序遍历
#根节点-左节点-右节点

def DLR_order(tree):
    if tree == None:
        return
    print(tree.data)
    DLR_order(tree.left)
    DLR_order(tree.right)

#中序遍历
#左节点-根节点-右节点

def LDR_order(tree):
    if tree == None:
        return
    LDR_order(tree.left)
    print(tree.data)
    LDR_order(tree.right)

#后序遍历
#左节点-右节点-根节点

def LRD_order(tree):
    if tree == None :
        return
    LRD_order(tree.left)
    LRD_order(tree.right)
    print(tree.data)

tree = node('d',node('b',node('a'),node('c')),node('e',right=node('g',node('f'))))

LDR_order(tree)