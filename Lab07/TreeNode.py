class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(root):
    if root is None:
        return -1  # Empty tree has height -1 by this definition
    return max(tree_height(root.left), tree_height(root.right)) + 1

def test_tree_height():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert tree_height(root) == 2
    
    # Test Case 2: Empty tree
    assert tree_height(None) == -1
    
    # Test Case 3: Single node tree
    assert tree_height(TreeNode(1)) == 0
    
    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    assert tree_height(left_skewed) == 3
    
    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    assert tree_height(perfect) == 2
    
    print(" All tests passed!")

test_tree_height()