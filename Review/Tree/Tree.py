#!/usr/bin/python

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class CommonTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = None



# 1. create bst based on array
def createBST(arr, start, end):

    if start > end:
        return None

    mid = (start + end) // 2
    root = TreeNode(arr[mid])
    root.left = createBST(arr, start, mid - 1)
    root.right = createBST(arr, mid + 1, end)

    return root

def createTree(arr):
    if not arr:
        return
    root = createBST(arr)

    return root


# 2. Height
def getHeight(root):

    if not root:
        return 0

    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)

    return 1 + max(leftHeight, rightHeight)

'''
# 3. Insert node

Note that how to use parent and current
'''
def insert(root, val):
    newNode = TreeNode(val)

    if not root:
        root = newNode
        return root

    parent = None
    current = root

    while 1:
        parent = current
        if current.val > val:
            current = current.left
            if not current:
                current.left = newNode
                return
        else:
            current = current.right
            if not current:
                current.right = newNode
                return

'''
4. Traverse_Recursion
'''
def preOrder(root):
    if root:
        print root.val
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print root.val
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print root.val

def DFS(root):
    if not root:
        return

    stack = [root]
    while stack:
        current = stack.pop()
        print "==> ", current.val
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

def BFS(root):
    if not root:
        return

    queue = [root]
    while queue:
        current = queue.pop(0)
        print "===> ", current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)



'''
5. Traverse_Iterative
'''
def preOrderIterative(root):

    if not root:
        return

    current = root
    stack = []

    while stack or current:
        while current:
            print current.val
            stack.append(current)
            current = current.left

        if stack:
            parent = stack.pop()
            current = current.right

def inOrderIterative(root):
    if not root:
        return

    current = root
    stack = []

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        if stack:
            current = stack.pop()
            print current.val
            current = current.right

def postOrderIterative(root):
    if not root:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        current = stack1.pop()
        stack2.append(current)

        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)

    while stack2:
        current = stack2.pop()
        print current.val


'''
6. Get one sequence from the other two [InOrder must in this two seq]
'''
def postSeq_pre_in_seq(preOrder, inOrder, postSeq):

    if not preOrder:
        return None
    if len(preOrder) == 1:
        return postSeq.append(preOrder)

    root = preOrder[0]
    root_index_in = inOrder.index(root)

    postSeq_pre_in_seq(preOrder[1: 1+root_index_in], inOrder[:root_index_in], postSeq)
    postSeq_pre_in_seq(preOrder[1+root_index_in:], inOrder[root_index_in+1:], postSeq)

    postSeq.append(root)

    return postSeq

def preSeq_in_post_seq(inOrder, postOrder, preSeq):
    if not postOrder:
        return

    if len(postOrder) == 1:
        return preSeq.append(postOrder)

    root = postOrder[-1]
    root_index_in = inOrder.index(root)

    preSeq.append(root)
    preSeq_in_post_seq(inOrder[:root_index_in], postOrder[:root_index_in], preSeq)
    preSeq_in_post_seq(inOrder[root_index_in + 1:], postOrder[root_index_in:-1], preSeq)

    return preSeq

'''
7. Check Balanced
'''
def checkHeight(root):
    if not root:
        return 0

    leftHeight = checkHeight(root.left)
    if leftHeight == -1:
        return -1

    rightHeight = checkHeight(root.right)
    if rightHeight == -1:
        return -1

    diff = abs(leftHeight - rightHeight)
    if diff > 1:
        return -1
    else:
        return max(leftHeight, rightHeight) + 1

def checkBalanced(root):
    if checkHeight(root) == -1:
        return False
    return True

'''
8. Create all lists based on depth of one tree. Note the differences between BFS
'''
def collectLevelList(root):
    if not root:
        return []

    result = []
    current = [root]

    while current:
        # result.append([node.val for node in current])
        result.append(current)
        parent = current
        current = []
        for child in parent:
            if child.left:
                current.append(child.left)
            if child.right:
                current.append(child.right)

    print result

'''
9. Check BST
'''
def inOrderBST(root, arr):
    if root:
        inOrderBST(root.left, arr)
        arr.append(root.val)
        inOrderBST(root.right, arr)

def checkBST(root):

    inOrderSeq = []
    inOrderBST(root, inOrderSeq)

    for i in range(len(inOrderSeq) - 1):
        if inOrderSeq[i + 1] < inOrderSeq[i]:
            return False

    return True

'''
10. InorderSucc [Mainly based on BST, otherwise there would be parent pointer]

Node InorderSucc(Node n):
    if n has right subtree:
        get left_most_child(n)
    else:
        # Note !!!
        while n is right of n.parent:
            n = n.parent
    
    return n.parent
    
'''
def getLeftMost(root):
    if not root:
        return None

    while root.left:
        root = root.left

    return root

# based on BST
def inorderSucc(root, node):
    if not root:
        return None

    if node.right:
        return getLeftMost(node.right)

    # use left to keep track of success node
    succ = None
    while root != node:
        if root.val < node.val:
            root = root.right
        else:
            succ = root
            root = root.left

    return succ


'''
11. Find path from root to target
    case1: binary
    case2: common tree
'''

def findPathBinaryTree(root, target, path, res):
    if not root:
        return

    path.append(root)
    print "val: ", root.val
    if root == target:
        print path
        res += path
        return

    if root.left:
        # here should not use return...
        findPathBinaryTree(root.left, target, path, res)
    if root.right:
        findPathBinaryTree(root.right, target, path, res)

    # Note that we should use pop
    path.pop()


def findPathTree(root, target, path, res):
    if not root:
        return

    path.append(root)

    if root == target:
        # for node in path:
        #     print node.val
        res += path
        return

    if root.children:
        for child in root.children:
            findPathTree(child, target, path, res)

    path.pop()

'''
12. LCA
# LCA
1. BST
2. Common binary Tree
3. Comman tree []
      [case1: has parent pointer => first common node of two linkedlist]
      [otherwise: find path from root to target respectively, then find common, like case1]
'''
def lca_bst(root, p, q):
    if not root:
        return None

    if p.val > q.val:
        return lca_bst(root, q, p)

    if root.val >= p.val and root.val <= q.val:
        return root

    if root.val < p.val:
        return lca_bst(root.right, p, q)
    if root.val > q.val:
        return lca_bst(root.left, p, q)

def lca_binaryTree(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lca_binaryTree(root.left, p, q)
    right = lca_binaryTree(root.right, p, q)

    if left and right:
        return root

    return left if left else right

# 1. need to find two paths end with p and q respectively
# 2. find the intersection of two linkedlist
def lca_commonTree(root, p, q):

    if not root:
        return None

    p_path = []
    findPathTree(root, p, [], p_path)

    q_path = []
    findPathTree(root, q, [], q_path)

    minLen = min(len(p_path), len(q_path))
    common = None

    for index in range(minLen):
        if p_path[index] != q_path[index]:
            print "common: ", common.val
            return common
        else:
            common = p_path[index]

'''
13. Subtree
'''
def subTree(root, q):
    if not root:
        return False

    if root.val == q.val:
        return check(root, q)

    return subTree(root.left, q) or subTree(root.right, q)


def check(p, q):
    if not p or not q:
        return not p and not q

    if p.val != q.val:
        return False

    return check(p.left, q.left) and check(p.right, q.right)

'''
14. Path sum I: is there any one path from root to leaf which sum to target
    Path sum II: print out all the paths from root to leaf
'''
#leetcode_112
def pathSum(root, sum):

    if not root:
        return False

    sum -= root.val
    if sum == 0 and not root.left and not root.right:
        return True
    if root.left and pathSum(root.left, sum):
        return True
    if root.right and pathSum(root.right, sum):
        return True
    return False


def helper(root, sum ,currrent, res):
    if not root:
        return

    sum -= root.val
    if sum == 0 and not root.left and not root.right:
        res.append(currrent + [root.val])
    if root.left:
        helper(root.left, sum, currrent + [root.val], res)
    if root.right:
        helper(root.right, sum, currrent + [root.val], res)

#leetcode_113
def pathSum2(root, sum, res):
    if not root:
        return

    result = []
    helper(root, sum, [], result)

    return result

'''
15. sum root to leaf
'''

def sumHelper(root, currentSum):
    if not root:
        return 0
    if not root.left and not root.right:
        return currentSum * 10 + root.val

    currentSum = currentSum * 10 + root.val

    return sumHelper(root.left, currentSum) + sumHelper(root.right, currentSum)

# leetcode_129
def sumRootToLeaf(root):

    res = sumHelper(root, 0)
    return res

'''
16. Verify post seq of bst
        5  OR   5
    4              7 
1                       8


'''
def verifyPostSeq(seq):

    # Note
    if not seq:
        return False

    root = seq[-1]
    index = 0

    # search left
    for index in range(len(seq)):
        if seq[index] > root:
            break

    # check right child
    for j in range(index, len(seq)):
        if seq[j] < root:
            return False

    left = True
    if index > 0:
        left = verifyPostSeq(seq[index:])

    right = True
    if index < len(seq) - 1:
        right = verifyPostSeq(seq[index:])

    return left and right

def verifyPreSeq(seq):
    if not seq:
        return False

    root = seq[0]
    index = None

    # search left
    for index in range(1, len(seq)):
        if seq[index] > root:
            break

    # search right
    for j in range(index, len(seq)):
        if seq[j] < root:
            return False

    left = True
    if index < len(seq) - 1:
        left = verifyPreSeq(seq[1:index])

    right = True
    if index < len(seq) - 1:
        right = verifyPreSeq(seq[index+1: ])

    return left and right


if __name__ == '__main__':
    '''
            50                  preOrder: 50, 30, 20, 15, 25, 40, 70, 60, 80
        30      70              inOrder: 15, 20, 25, 30, 40, 50, 60, 70, 80
    20    40  60  80            postOrder: 15, 25, 20, 40, 30, 60, 80, 70, 50
   15 25                        DFS: 50, 30, 20, 15, 25, 40, 70, 60, 80
                                BFS: 50, 30, 70, 20, 40, 60, 80, 15, 25
    '''

    '''
    ########### DEMO OF BINARY TREE ###########
    
    node1 = TreeNode(50)
    node2 = TreeNode(30)
    node3 = TreeNode(70)
    node4 = TreeNode(20)
    node5 = TreeNode(40)
    node6 = TreeNode(60)
    node7 = TreeNode(80)
    node8 = TreeNode(15)
    node9 = TreeNode(25)

    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9


    findPathBinaryTree(node1, node9, [])

    # succ = inorderSucc(node1, node5)
    # print succ.val

    # collectLevelList(node1)
    '''

    '''
    ########### DEMO OF COMMON TREE ###########
    
    node1 = CommonTreeNode(50)
    node2 = CommonTreeNode(30)
    node3 = CommonTreeNode(70)
    node4 = CommonTreeNode(20)
    node5 = CommonTreeNode(40)
    node6 = CommonTreeNode(60)
    node7 = CommonTreeNode(80)
    node8 = CommonTreeNode(15)
    node9 = CommonTreeNode(25)

    node1.children = [node2, node3]
    node2.children = [node4, node5]
    node3.children = [node6, node7]
    node4.children = [node8, node9]

    # res = []
    # findPathTree(node1, node9, [], res)
    # for node in res:
    #     print node.val

    lca_commonTree(node1, node8, node5)
    '''









