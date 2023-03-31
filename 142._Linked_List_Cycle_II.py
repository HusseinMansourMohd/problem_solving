# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = set()
        index = []
        current = head
        count = 0
        while current:
            if current not in values:
                values.add(current)
            else:
                return pos
        count += 1
