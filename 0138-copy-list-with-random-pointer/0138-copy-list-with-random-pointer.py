"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node_dict = dict()
        cur = head
        while cur:
            new = Node(cur.val, None, None)
            node_dict[cur] = new
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                node_dict[cur].next = node_dict[cur.next]
            if cur.random:
                node_dict[cur].random = node_dict[cur.random]
            
            cur = cur.next
        
        return node_dict[head]