# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        new = head
        count = 0
        while current:
            current = current.next
            count += 1
        for i in range(0,count//2):
            new = new.next
        return new