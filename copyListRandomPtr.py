# Time:
# Space:
# Leetcode:
# Issues:

class Solution:
    def __init__(self):
        self.hmap = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        #pass 1
        while curr:
            self.clone(curr) 
            curr = curr.next
        #pass 2
        curr = head
        while curr:
            copyCurr = self.hmap[curr]
            copyCurr.next = self.clone(curr.next)
            copyCurr.random = self.clone(curr.random)
            curr = curr.next

        return self.hmap[head]

    def clone(self, node):
        if not node: return 

        if node not in self.hmap:
            self.hmap[node] = node.val

        return self.hmap[node]
