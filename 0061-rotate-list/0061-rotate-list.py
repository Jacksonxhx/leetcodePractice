# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        将链表先连成环，然后将链表在指定位置断开。
        遍历到 size - k % size 的位置，记录下断开后新链表头节点位置，再将其断开并返回新的头节点。
        '''
        # 初始判断
        if k == 0 or not head or not head.next:
            return head
        # 设定size和walk
        size = 1
        walk = head
        # 记录size
        while walk.next:
            walk = walk.next
            size += 1
        # 形成环，walk的下一个node指向链表头
        walk.next = head
        # 得到新链表的表头位置
        k = size - k % size
        # 循环k次，把walk走到新链表的队尾
        while k:
            walk = walk.next
            k -= 1
        # 记录新的链表头
        newHead = walk.next
        # 断掉新链表的队尾
        walk.next = None
        
        return newHead
        
                