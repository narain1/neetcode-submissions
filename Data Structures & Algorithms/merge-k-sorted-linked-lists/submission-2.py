# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapNode:
    def __init__(self, node):
        self.val = node.val
        self.next = node.next

    def __lt__(self, other):
        return self.val <= other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ptr = ListNode()    
        dummy = ptr

        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, HeapNode(l))

        while heap:
            node = heapq.heappop(heap)
            ptr.next = ListNode(node.val)
            ptr = ptr.next

            if node.next:
                heapq.heappush(heap, HeapNode(node.next))
            
        return dummy.next

