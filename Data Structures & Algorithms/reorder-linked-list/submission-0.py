# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        half_pos, full = head, head

        while full.next and full.next.next:
            full = full.next.next
            half_pos = half_pos.next

        # reversing the link list
        second = half_pos.next
        half_pos.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev

            prev = second
            second = tmp

        # half_pos contains the last element
        # now we need to interlink the nodes

        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
            