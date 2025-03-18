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