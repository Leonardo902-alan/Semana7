class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirror_tree(root):
    if root is None:
        return None
    
    # Create a new node with swapped children
    mirrored = TreeNode(root.val)
    mirrored.left = mirror_tree(root.right)
    mirrored.right = mirror_tree(root.left)
    
    return mirrored

def test_mirror_tree():
    # Helper function to compare tree structure
    def trees_equal(a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return (a.val == b.val and 
                trees_equal(a.left, b.left) and 
                trees_equal(a.right, b.right))
    
    # Test Case 1: Normal tree
    original = TreeNode(1)
    original.left = TreeNode(2)
    original.right = TreeNode(3)
    original.left.left = TreeNode(4)
    original.left.right = TreeNode(5)
    
    mirrored = mirror_tree(original)
    
    # Expected mirrored tree
    expected = TreeNode(1)
    expected.left = TreeNode(3)
    expected.right = TreeNode(2)
    expected.right.left = TreeNode(5)
    expected.right.right = TreeNode(4)
    
    assert trees_equal(mirrored, expected), "Test Case 1 Failed"
    
    # Test Case 2: Empty tree
    assert mirror_tree(None) is None, "Test Case 2 Failed"
    
    # Test Case 3: Single node tree
    assert trees_equal(mirror_tree(TreeNode(1)), TreeNode(1)), "Test Case 3 Failed"
    
    # Test Case 4: Left-only tree
    left_only = TreeNode(1)
    left_only.left = TreeNode(2)
    left_only.left.left = TreeNode(3)
    mirrored_left = mirror_tree(left_only)
    expected_left = TreeNode(1)
    expected_left.right = TreeNode(2)
    expected_left.right.right = TreeNode(3)
    assert trees_equal(mirrored_left, expected_left), "Test Case 4 Failed"
    
    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    mirrored_perfect = mirror_tree(perfect)
    expected_perfect = TreeNode(1)
    expected_perfect.left = TreeNode(3)
    expected_perfect.right = TreeNode(2)
    expected_perfect.left.left = TreeNode(7)
    expected_perfect.left.right = TreeNode(6)
    expected_perfect.right.left = TreeNode(5)
    expected_perfect.right.right = TreeNode(4)
    assert trees_equal(mirrored_perfect, expected_perfect), "Test Case 5 Failed"
    
    print(" All tests passed!")

test_mirror_tree()