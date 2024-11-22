# Initialize the parent, size and height arrays
parent = list(range(13))  # We'll assume 13 elements (from 0 to 12)
size = [1] * 13  # Initially, each element is in a set of size 1
height = [1] * 13  # Initially, each element is in a tree of height 1

# Find with path compression (for part c)
def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])  # Path compression
    return parent[i]

# Union by size (part a)
def union_by_size(i, j):
    root_i = find(i)
    root_j = find(j)
    
    if root_i != root_j:
        # Union by size: attach the smaller tree to the larger one
        if size[root_i] < size[root_j]:
            parent[root_i] = root_j
            size[root_j] += size[root_i]
        else:
            parent[root_j] = root_i
            size[root_i] += size[root_j]

# Union by height (part b)
def union_by_height(i, j):
    root_i = find(i)
    root_j = find(j)
    
    if root_i != root_j:
        # Union by height: attach the shorter tree to the taller one
        if height[root_i] < height[root_j]:
            parent[root_i] = root_j
        elif height[root_i] > height[root_j]:
            parent[root_j] = root_i
        else:
            parent[root_j] = root_i
            height[root_i] += 1

# Union by size with path compression (part c)
def union_by_size_with_compression(i, j):
    root_i = find(i)
    root_j = find(j)
    
    if root_i != root_j:
        # Union by size: attach the smaller tree to the larger one
        if size[root_i] < size[root_j]:
            parent[root_i] = root_j
            size[root_j] += size[root_i]
        else:
            parent[root_j] = root_i
            size[root_i] += size[root_j]

# Perform the sequence of union operations
def apply_operations():
    operations = [
        (1, 2), (3, 4), (3, 5), (1, 7), 
        (3, 12), (0, 9), (8, 10), (8, 9), 
        (7, 4), (2, 9)
    ]

    # Part (a) Union by size
    # Reset parent and size arrays for part (a)
    global parent, size, height
    parent = list(range(13))
    size = [1] * 13
    for i, j in operations:
        union_by_size(i, j)
    print("Union by Size Parent Map:", parent)

    # Part (b) Union by height
    # Reset parent and height arrays for part (b)
    parent = list(range(13))
    height = [1] * 13
    for i, j in operations:
        union_by_height(i, j)
    print("Union by Height Parent Map:", parent)

    # Part (c) Union by size with path compression
    # Reset parent and size arrays for part (c)
    parent = list(range(13))
    size = [1] * 13
    for i, j in operations:
        union_by_size_with_compression(i, j)
    print("Union by Size with Path Compression Parent Map:", parent)

# Run the operations and display the results
apply_operations()
