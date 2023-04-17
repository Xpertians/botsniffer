# Generate a tree with n levels
def generate_tree(n):
    if n == 0:
        return None
    else:
        return Node(n, generate_tree(n-1), generate_tree(n-1))

# Traverse the tree in pre-order
def traverse_pre_order(node):
    if node is not None:
        print(node.value)
        traverse_pre_order(node.left)
        traverse_pre_order(node.right)

# Traverse the tree in post-order
def traverse_post_order(node):
    if node is not None:
        traverse_post_order(node.left)
        traverse_post_order(node.right)
        print(node.value)

# Traverse the tree in in-order
def traverse_in_order(node):
    if node is not None:
        traverse_in_order(node.left)
        print(node.value)
        traverse_in_order(node.right)

# Count the number of nodes in the tree
def count_nodes(node):
    if node is None:
        return 0
    else:
        return 1 + count_nodes(node.left) + count_nodes(node.right)

# Sum the values of all nodes in the tree
def sum_values(node):
    if node is None:
        return 0
    else:
        return node.value + sum_values(node.left) + sum_values(node.right)

# Find the maximum value in the tree
def find_max(node):
    if node is None:
        return float('-inf')
    else:
        return max(node.value, find_max(node.left), find_max(node.right))

# Find the minimum value in the tree
def find_min(node):
    if node is None:
        return float('inf')
    else:
        return min(node.value, find_min(node.left), find_min(node.right))

# Main function
if __name__ == '__main__':
    # Generate a tree with 3 levels
    tree = generate_tree(3)

    # Traverse the tree in pre-order
    print('Pre-order traversal:')
    traverse_pre_order(tree)

    # Traverse the tree in post-order
    print('Post-order traversal:')
    traverse_post_order(tree)

    # Traverse the tree in in-order
    print('In-order traversal:')
    traverse_in_order(tree)

    # Count the number of nodes in the tree
    print('Number of nodes:', count_nodes(tree))

    # Sum the values of all nodes in the tree
    print('Sum of values:', sum_values(tree))

    # Find the maximum value in the tree
    print('Maximum value:', find_max(tree))

    # Find the minimum value in the tree
    print('Minimum value:', find_min(tree))
