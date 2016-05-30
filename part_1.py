# Part 1: Discussion Questions

# Runtime

# Q: When calculating the Big O notation for a particular algorithm, it's necessary
# to consider the length of time it takes for the algorithm to run as the algorithm's
# workload approaches the size of infinity. What is the workload of a function that
# takes in a list of integers and returns a new list of the even integers?
# A: 

# Q: Order the following runtimes in ascending order by efficiency as n approaches infinity:
# O(log n),
# O(n^2)
# O(n log n)
# O(n)
# O(2^n)
# O(1)

# A:
# O(2^n)
# O(n^2)
# O(n log n)
# O(n)
# O(log n),
# O(1)



# Stacks and Queues

# Q: In the following cases, would a stack or queue be an appropriate data structure?
# q0: The process of loading and unloading pallets onto a flatbed truck
# q1: Putting bottle caps on bottles of beer as they roll down an assembly line
# q2: Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2)
# A: stack, queue, tree or stack

# Q: Describe 2 more examples of when a queue would be an appropriate data structure.
# A: netflix dvd rental, waiting at a stoplight
# Q: Describe 2 more examples of when a stack would be an appropriate data structure.
# A: cleaning my room, making scrapbooks


# Linked Lists

# Q: Given the below linked list,
# q0: which are the nodes?
# q1: What is the data for each node?
# q2: Where is the head?
# q3: Where is the tail? (Please be as specific as possible - exactly
# which parts of the diagram correspond to each part? Arrows? Boxes? Text?)
# A:
# a0: the box containing "Apple" and next, the box containing "Berry" and
#     next, the box containing "Cherry" and next
# a1: "Apple", "Berry", "Cherry"
# a2: the head is whatever the arrow from the box containing head points
#     to. In this case, the "Apple" node
# a3: the tail is whichever node that  does not hoave a following node.
#     In this case, it is the "Cherry" node

# Q: What's the difference between a doubly and singly linked list?
# A: In a singly-linked list, each node knows the node following it. In
#    a doubly linked list, each node knows the nodes previous to it and
#    following it
# Q: Why is it faster to append to a linked list if we keep track of the
# tail as an attribute?
# A: Because then we can access the tail in constant time since
# we know exactly where it is. If we need to add an element, we'd
# only re-index two elements



# Trees


# Q: Given the above tree, in what order would a Breadth First Search (BFS)
# algorithm visit each node until finding burrito (starting at food)?
# A: food, italian, indian, mexican, lasagna, tikka masala, saag, burrito

# Given the above tree, in what order would a Depth First Search algorithm
# visit each node until finding Chicago-style (starting at food)?
# A: food, mexican, enchiladas, tacos, burritos, indian, saag, tikka masala,
# italian, pizza, sicilian, new-york style, chicago-style

# How is a binary search tree different from other trees?
# A: a binary search tree (for well-balanced binary trees)
# will reduce the possible work to do by half (O(log n) runtime)
# because it only follows the most relevant child for each node it checks



























