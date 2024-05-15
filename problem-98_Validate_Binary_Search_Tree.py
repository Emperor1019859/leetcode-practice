"""
# Medium
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # TODO: refactor
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        current_node = root
        queue = [root]

        while queue:
            if current_node.left:
                if current_node.left.val >= current_node.val:
                    return False

                right_node = current_node.left.right

                while right_node:
                    if right_node.val >= current_node.val:
                        return False
                    right_node = right_node.right

                queue.append(current_node.left)

            if current_node.right:
                if current_node.right.val <= current_node.val:
                    return False

                left_node = current_node.right.left

                while left_node:
                    if left_node.val <= current_node.val:
                        return False
                    left_node = left_node.left

                queue.append(current_node.right)

            queue.pop(0)
            current_node = queue[0] if queue else None

        return True


left_node = TreeNode(val=1)
right_node = TreeNode(val=3)
root = TreeNode(val=2, left=left_node, right=right_node)

answer = Solution().isValidBST(root)
print(answer)  # True

# Runtime 68 ms Beats 5.34% of users with Python3
# Memory 18.63 MB Beats 13.02% of users with Python3
