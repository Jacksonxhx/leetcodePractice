# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        反过来遍历，如果当前value大于cur max留下不然删掉
        """
        # reverse the linked list
        prev = None
        curr = head
        
        while curr:
            # 保存下一个节点
            next_node = curr.next
            # 将当前节点的next指向上一个节点
            curr.next = prev
            # 将prev更新成curr
            prev = curr
            # 更新curr
            curr = next_node
        
        cur_max = prev.val
        walk = prev
        while walk.next:
            if walk.next.val < cur_max:
                walk.next = walk.next.next
                continue
            else:
                cur_max = walk.next.val
            walk = walk.next
        
        head = prev
        
        prev = None
        curr = head
        
        while curr:
            # 保存下一个节点
            next_node = curr.next
            # 将当前节点的next指向上一个节点
            curr.next = prev
            # 将prev更新成curr
            prev = curr
            # 更新curr
            curr = next_node
        
        return prev