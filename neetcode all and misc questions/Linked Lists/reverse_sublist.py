"""
You are maintaining a linked sequence of shipment manifest records in a logistics application where specific sub-batches need to be reversed in-place during sorting operations. Write a function that takes the head of a linked list along with two 1-indexed integers representing a start position and an end position, and reverses the nodes of the list from the start position to the end position in-place. Return the head of the modified linked list.

Function signature:

reverseSublist(head: linked list of integers, start: integer, end: integer) -> linked list of integers
Example 1:

Input: head = [1, 2, 3, 4, 5], start = 2, end = 4
Result: [1, 4, 3, 2, 5]
Explanation: Reversing the sublist from position 2 to 4 in the list [1, 2, 3, 4, 5] yields [1, 4, 3, 2, 5].

Example 2:

Input: head = [5, 10], start = 1, end = 2
Result: [10, 5]
Explanation: Reversing the sublist from position 1 to 2 in the list [5, 10] yields [10, 5].

Constraints:
- The number of nodes in the list is between 1 and 500.
- 1 <= start <= end <= number of nodes

"""
class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def print_list(head):
    while (head):
        print(head.value)
        head = head.next
        
def reverse_sublist(head: ListNode, start: int, end: int) -> ListNode:
    # create a dummy node where the next points to the head
    # this is so that if the start position is 1, we can use the dummy node as the "before"
    # otherwise we wouldn't have a node right before the start position and before.next would be null
    dummy = ListNode(0)
    dummy.next = head
    before = dummy
    pos = 1
    # find the node right before the start position
    for _ in range(start - 1):
        before = before.next
    prev = None
    temp = None
    # stash the value of before.next, which is the actual starting position for the reverse 
    tail = before.next
    reverse_head = before.next
    # from start to end + 1, reverse
    for i in range(start, end+1):
        if reverse_head:
            temp = reverse_head
            reverse_head = reverse_head.next
            temp.next = prev
            prev = temp
    # prev is now the head of the reversed list, set to before.next
    # before is pointing at 1
    # i.e 1 -> [4 -> 3 -> 2]
    before.next = prev
    # we need to re-attach the "ending" portion, which is what reverse_head ends up being after the reversing ends
    # 2 -> 5 ...
    tail.next = reverse_head
    return dummy.next


n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print("test case 1")
head = reverse_sublist(n, 2,4)
print_list(head)
print("test case 2")
n2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
new_head = reverse_sublist(n2, 1,3)
print_list(new_head)


    
            
