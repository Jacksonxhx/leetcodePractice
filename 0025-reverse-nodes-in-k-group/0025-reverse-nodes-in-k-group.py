# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        用index %= k 来判断是否到需要换的地方
        用一个区间，在这个区间做转换
        比如 1->2->3，就先换1，2变成 2->1->3
        然后换2，3变成3->2->1
        '''
        # 创造一个dummy用来创造cur和tail区间
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        tail = dummy.next
        index = 0
        
        # 如果是到了要reverse的点，reverse
        while tail:
            # 用index判断
            index += 1
            if index % k == 0:
                cur = self.reverse(cur, tail.next)
                tail = cur.next
            # 不然进一位
            else:
                tail = tail.next
                
        return dummy.next
                
    
    # head, tail为reverse区间上下两点
    # 相当于把head一直往前送
    def reverse(self, head, tail):
        # pre指向需要反转的点的前一个点
        pre = head
        # cur指向需要反转的点
        cur = pre.next
        first = cur
        while cur is not tail:
            # 存cur next
            next = cur.next
            # cur到pre前
            cur.next = pre
            # pre往前走一个
            pre = cur
            # cur往后走一个
            cur = next
        head.next = pre
        first.next = tail
        
        return first