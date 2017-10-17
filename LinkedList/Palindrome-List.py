'''
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
'''
def isPalindrome(self,head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next
    while prev:
        if prev.val != head.val:
            return 0
        prev = prev.next
        head = head.next
    return 1
