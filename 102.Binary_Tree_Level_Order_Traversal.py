"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#####

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Add children from right to  left so they are processed in the correct order
            for child in reversed(node.children):
                stack.append(child)
        
        return result