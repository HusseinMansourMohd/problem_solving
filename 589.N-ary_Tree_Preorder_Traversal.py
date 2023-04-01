"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        current = root
        output = []

        while current:
            if current not in output:
                output.append(current)
            if current.children:
                output.append(current.children)
        return output
