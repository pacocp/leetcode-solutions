class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        number_of_nodes = 0
        current = head
        while current:
            current = current.next
            number_of_nodes += 1

        middle = number_of_nodes // 2

        current = head
        for i in range(middle):
            current = current.next
        
        return current
