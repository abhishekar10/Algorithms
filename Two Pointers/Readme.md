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

<h4>3. Valid Palindrome</h4>
<p>
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</p>

<b>Solution:</b>

- **Filters Non-Alphanumeric Characters Twice**: Removes all non-alphanumeric characters separately for both the original and reversed strings.  
- **Converts to Lowercase After Reversing**: Ensures case insensitivity by applying `.lower()` after reversing the string.  
- **Checks for Palindrome**: Compares the processed string with its reversed version.  

<h4>4. Two Sum - Sorted</h4>
<p>
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
</p>

<b>Solution:</b>
- **Uses Two Pointers Approach**: Maintains two pointers, one at the start (`l`) and one at the end (`r`) of the sorted array.  
- **Calculates Sum Iteratively**: Computes the sum of `numbers[l]` and `numbers[r]` in each iteration.  
- **Adjusts Pointers Efficiently**: Moves the left pointer right if the sum is too small and moves the right pointer left if the sum is too large.  
- **Returns 1-Based Indices**: When a match is found, returns the indices as per the 1-based indexing requirement.  

<h4>Three Sum</h4>
<p>
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
</p>

<b>Solution:</b>
- **Sorts the Input Array**: Sorting ensures efficient two-pointer traversal for finding triplets.  
- **Iterates with a Fixed First Element**: Uses a loop to fix one number and then applies the two-pointer technique to find pairs that sum to zero.  
- **Avoids Duplicates**: Skips over duplicate elements to prevent duplicate triplets in the result.  
- **Uses Two Pointers for Efficient Searching**: Adjusts left (`l`) and right (`r`) pointers to find valid triplets without unnecessary iterations.  
