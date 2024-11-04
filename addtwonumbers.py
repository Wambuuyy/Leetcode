"""
I am given two reversed linked list I am supposed to add corresponding numbers and return the nswer in a reversed linked list too...
 I should also handle carry
First initialize new linked list to store the new values
Iterate through linked lists and carry provided they are not empty
add the values and also carry if there is one...
if the anser from addition is more than 10 get carry by dividing by 10
find new value by getting modulo of 10
update values in the new linkd list and move the node and repeat the loop
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum = val1 + val2 + carry
        carry = sum // 10
        new_val = sum % 10

        current.next = ListNode(new_val)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

# Helper function to convert a list to a linked list
def to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print a linked list as a list of values
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

l1 = to_linked_list([2, 4, 3])
l2 = to_linked_list([5, 6, 4])
result = addTwoNumbers(l1, l2)
print(print_linked_list(result))

l4 = to_linked_list([0])
l5 = to_linked_list([0])
result = addTwoNumbers(l4, l5)
print(print_linked_list(result))

l6 = to_linked_list([9, 9, 9, 9, 9, 9, 9])
l7 = to_linked_list([9, 9, 9, 9])
result = addTwoNumbers(l6, l7)
print(print_linked_list(result))