# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        二分加归并
        '''
        if not lists:
            return None
        size = len(lists)
        return self.merge_sort(lists, 0, size - 1)
        
    def merge(self, a: ListNode, b: ListNode):
        root = ListNode(-1)
        cur = root
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        if a:
            cur.next = a
        if b:
            cur.next = b
            
        return root.next
    
    def merge_sort(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        left_node = self.merge_sort(lists, left, mid)
        right_node = self.merge_sort(lists, mid + 1, right)
        return self.merge(left_node, right_node)