'''
Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.
'''
def delete_node(node_to_delete):
    next_node = node_to_delete.next

    if next_node:
        node_to_delete.val = next_node.val
        node_to_delete.next = next_node.next

    else:
        raise Exception("Can't delete it dude")
