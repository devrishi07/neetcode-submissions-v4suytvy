class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None


        for i in range(1, len(lists)):
            lists[i] = self.merge(lists[i - 1], lists[i])
            
                
        
        return lists[-1]



    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        curr = dummy = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            
            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next    
            

        