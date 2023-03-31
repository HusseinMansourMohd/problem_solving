# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        current = head
        count = 0
        while current:
            if current not in dic:
                dic[str(current)] = count 
                current = current.next
            else:
                return dic.get(str(current))
            count += 1
