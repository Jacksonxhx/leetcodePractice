# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 定义dummy
        fdum, bdum = ListNode(0), ListNode(0)
        # 定义三个指针
        front, back, curr = fdum, bdum, head
        
        # 遍历一遍head
        while curr != None:
            if curr.val < x:
                # 逻辑是：将 curr 节点添加到 front 链表的末尾，并移动 front 指针。
                front.next = curr
                front = curr
            else:
                back.next = curr
                back = curr
            # 更新curr，但注意front和back是不会变的
            curr = curr.next
        
        front.next, back.next = bdum.next, None
        
        return fdum.next