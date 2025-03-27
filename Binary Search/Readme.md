<h1>Problems</h1>

<h4>1. Binary Search</h4>
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

<b>Solution Explanation:</b>
- **Implements Binary Search**: Uses a two-pointer approach (`l` and `r`) to efficiently find the target.  
- **Calculates Midpoint Iteratively**: Computes `mid = (l + r) // 2` in each iteration to narrow the search range.  
- **Adjusts Search Range Based on Comparison**: Moves `l` or `r` depending on whether `nums[mid]` is smaller or larger than the target.  
- **Runs in O(log n) Time Complexity**: Efficient for large sorted arrays due to logarithmic search behavior.

<h4>Search a 2-D Matrix</h4>
<p>
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1 :
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2 :
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
</p>

<b>Solution Explanation</b>
- **Uses Binary Search on a 2D Matrix**: Treats the matrix as a flattened sorted array for efficient searching.  
- **Calculates Midpoint Efficiently**: Converts the 1D index to 2D coordinates using `divmod(mid, n)`.  
- **Adjusts Search Range Based on Comparison**: Moves `left` or `right` depending on whether `matrix[mid_row][mid_col]` is smaller or larger than the target.  
- **Runs in O(log(m * n)) Time Complexity**: Optimized approach for searching in a sorted matrix.  