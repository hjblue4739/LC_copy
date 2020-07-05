## Binary Tree Traversal
- (95) Unique Binary Search Trees II  
    Binary tree inorder traversal with the time complexity of O(4^n), this is because the problem meets the Segner's recurrent relation:
    C_0 = 1 and C_(n+1) is the sum of C_i*C_(n-i) where i is in the range of 0 to n.
    
- (105) Construc Binary Tree from Inorder 
- (106) Construct Binary Tree from Inorder and Postorder Traversal  
    Due to postorder, the traversal order is `left->right->root`, when we construct the tree with the value from list of postorder, we need to the follow the order of `root->right->left`.
- (107) Binary Tree Level Order Traversal II   
    BFS uses `deque` to pop the left element and add to the right.


# Based on Solution
## Kth Problem
- (378) Kth Smallest Element in a Sorted Matrix
- (Lintcode 465) Kth Smallest Sum in Two Sorted Arrays

## Two Pointers of Same Direction
- (3) Longest Substring Without Repeating Characters
- (209) Minimum Size Subarray Sum
- (340) Longest Substring with At Most K Distinct Characters

## Union Find
- (261) Graph Valid Tree
- (305) Number of Island II
- (Lintcode 590) Connecting Graph II
- (Lintcode 629) Minimum Spanning Tree
- (721) Accounts Merge

## Trie
- (208) Implement Trie (Prefix Tree)
- (211) Add and Search Word - Data structure design
- (212) Word Search II

## Prefix Sum
- (Lintcode 138) Subarray Sum
- (Lintcode 405) Submatrix Sum

## Stack
- (155) Min Stack
- (394) Decode String
- (654) Maximum Binary Tree
- (Lintcode 22) Flatten List
- (Lintcode 402) Continuous Subarray Sum

# Stack + Design
- (341) Flatten Nested List Iterator

## Monotone Stack
- (42) Trapping Rain Water
- (84) Largest Rectangle in Histogram
- (85) Maximal Rectangle

## Two Heaps - minHeap and maxHeap
- (295) Find Median from Data Stream
- (480) Sliding Window Median

## Min Heap
- (407) Trapping Rain Water II

## Sweep Line
- (253) Meeting Rooms II
- (Lintcode 391) Number of Airplanes in the Skyline

## Binary Search
- (29) Divide Two Integers
- (69) Sqrt(x)
- (287) Find the Duplicate Number
- (644) Maximum Average Subarray II
- (Lintcode 183) Wood Cut
- (Lintcode 437) Copy Books
- (Lintcode 586) Sqrt(x) II

## Deque
- (239) Sliding Window Maximum
- (346) Moving Average from Data Stream

## Dynamic Programming
- (198) House Robber

## DFS + Binary Tree



