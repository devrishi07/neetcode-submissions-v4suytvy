class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None}

        curr = head

        while curr: 
            new = Node(curr.val)
            hashmap[curr] = new
            curr = curr.next
        
        curr = head
        while curr:
            node = hashmap[curr]
            node.next =  hashmap[curr.next]
            node.random = hashmap[curr.random]
            curr = curr.next
        
        return hashmap[head]



         