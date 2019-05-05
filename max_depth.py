'''

'''

# Definition for a binary tree node.
#class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		def is_leaf(leaf) -> bool:
			if not leaf:
				return False
			if type(leaf) is TreeNode and not leaf.left and not leaf.right:
				return True
			else:
				return False
		if root is None:
			return 0
		if is_leaf(root):
			return 1

		return max(self.maxDepth(root.left).self.maxDepth(root.right)) + 1
