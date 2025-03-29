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

<h4>2. Search a 2-D Matrix</h4>
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

<h4>3. Koko eating bananas</h4>
<p>
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
</p>

<b>Solution Explanation:</b>
- **Uses Binary Search on Eating Speed**: Searches for the minimum possible eating speed (`k`) within the range `[1, max(piles)]`.  
- **Calculates Total Hours Needed for a Given Speed**: Iterates through `piles`, using `math.ceil(piles[i] / mid)` to determine the hours taken at speed `mid`.  
- **Adjusts Search Range Based on Time Constraint**: If the total hours taken is within `h`, reduces the upper bound (`r`), otherwise increases the lower bound (`l`).  
- **Optimized O(n log max(piles)) Solution**: Efficiently finds the minimum speed while ensuring all bananas are eaten within `h` hours.

<h4>4. Minimum in rotated sorted array</h4>
<p>
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
</p>

<b>Solution Explanation</b>
- **Uses Binary Search on Rotated Sorted Array**: Searches for the minimum element efficiently using binary search.
- **Initializes Pointers and a Result Variable**: Uses `l = 0`, `r = len(nums) - 1`, and `res = float(inf)` to track the minimum value.
- **Checks Middle Element and Updates Minimum**: Compares `nums[m]` with `res` to keep track of the smallest value found.
- **Adjusts Search Range Based on Rotation**: Moves `l` right if `nums[m] > nums[r]`, otherwise moves `r` left.
- **Optimized O(log n) Solution**: Finds the minimum element in logarithmic time using binary search.