<h1>Problems</h1>
<h4>1.Move Zeroes:</h4>
<b>Problem Description:</b>
<p>

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]
</p>

<b>Solution:</b>
- Uses a two-pointer approach (`l` and `r`) to move non-zero elements forward.
- Swaps elements when a non-zero is found, maintaining order.
- Ensures all zeroes are pushed to the end in a single pass.
- Runs in O(n) time and O(1) space, modifying the list in-place.

<h4>2.Cotainer with most water:</h4>
<p>
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
</p>

<b>Solution:</b>

- Uses a two-pointer approach (`l` at the start, `r` at the end) to find the max water container area.  
- Calculates the area based on the shorter height between `l` and `r`, updating the max area found.  
- Moves the pointer pointing to the smaller height to potentially find a larger area.  
- Runs in **O(n) time** and **O(1) space**, ensuring an efficient solution. 