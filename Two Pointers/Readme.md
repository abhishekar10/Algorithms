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