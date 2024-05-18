# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        对于链表进行merge sort
        '''
        return self.mergeSort(head)
    
    def mergeSort(self, head):
        '''
        切割链表，recursion直到
        '''
        # 如果链表没有或者长度是1的情况
        if not head or not head.next:
            return head
        
        # 用快慢walk找到mid node，slow就是中间的node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 分割单链表变成两个链表
        left, right = head, slow.next
        slow.next = None
        
        return self.merge(self.mergeSort(left), self.mergeSort(right))
    
    
    def merge(self, left, right):
        '''
        合并链表
        '''
        new = ListNode(-1)
        dummy = new
        
        while left and right:
            if left.val <= right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next
        
        if left:
            dummy.next = left
        elif right:
            dummy.next = right
        
        return new.next
        