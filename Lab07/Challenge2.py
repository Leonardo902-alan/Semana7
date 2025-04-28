class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

def test_count_leaves():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert count_leaves(root) == 3
    
    # Test Case 2: Empty tree
    empty_tree = None
    assert count_leaves(empty_tree) == 0
    
    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    assert count_leaves(single_node) == 1
    
    # Test Case 4: No leaf nodes at first level
    no_leaves_at_first = TreeNode(1)
    no_leaves_at_first.left = TreeNode(2)
    no_leaves_at_first.right = TreeNode(3)
    assert count_leaves(no_leaves_at_first) == 2
    
    # Test Case 5: All nodes are leaves except root
    all_leaves = TreeNode(1)
    all_leaves.left = TreeNode(2)
    all_leaves.right = TreeNode(3)
    all_leaves.left.left = TreeNode(4)
    all_leaves.left.right = TreeNode(5)
    all_leaves.right.left = TreeNode(6)
    all_leaves.right.right = TreeNode(7)
    assert count_leaves(all_leaves) == 4
    
    print("✅ All tests passed!")

test_count_leaves()