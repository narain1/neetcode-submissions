# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        min_heap = []

        for idx, l in enumerate(lists):
            if l is not None:
                heapq.heappush(min_heap, (l.val, idx, l))

        dummy = ListNode(0)
        cur = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            cur.next = ListNode(val)
            cur = cur.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        return dummy.next