# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101) #创造出一个Node一直记录答案
        Node = dummy #这个Node是一个指针，一直变化，作用就是找到下一个值该是什么
        
        #遍历两个链表
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                Node.next = list1 #Node的next就是找到下一个该是哪个节点，相当于是把dummy.next变成list1当前的值
                list1 = list1.next #更新list1
                
            else:
                Node.next = list2 #Node的next就是找到下一个该是哪个节点
                list2 = list2.next #更新list2
            Node = Node.next #更新Node，同时相当于更新dummy

        #查漏补缺
        if list1 is not None:
            Node.next = list1
        else:
            Node.next = list2
            
        #返回结果
        return dummy.next
            
