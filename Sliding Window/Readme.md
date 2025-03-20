<h1>Problems</h1>

<h4>1. Best time to buy and sell stock</h4>
<p>
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
</p>

<b>Solution Explanation: </b>
- **Uses Two Pointers (`l` and `r`)**: `l` tracks the buying day, while `r` scans for a potential selling day.  
- **Calculates Maximum Profit**: Computes the difference between `prices[r]` and `prices[l]`, updating the profit if a higher value is found.  
- **Adjusts Buying Point When Needed**: Moves `l` to `r` when a lower price is found, ensuring the best buy price is always chosen.  
- **Optimized O(n) Solution**: Traverses the list once, making it efficient for large datasets. 

<h4>2. Longest substring without repeating characters</h4>
<p>
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
</p>

<b>Solution Explanation:</b>
- **Uses Sliding Window Approach**: Expands the right pointer (`r`) while adjusting the left pointer (`l`) to maintain a unique character set.  
- **Utilizes a Set for Fast Lookups**: Stores characters in a set (`c`) to efficiently check for duplicates.  
- **Dynamically Updates Maximum Length**: Updates `result` whenever a longer substring without repeating characters is found.  
- **Optimized O(n) Time Complexity**: Each character is processed at most twice, making it efficient for large inputs.

<h4>Maximum Average Subarray - I</h4>
<p>
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
</p>

<b>Solution Explanation :</b>
- **Uses Sliding Window Technique**: Maintains a window of size `k` and updates its sum dynamically.  
- **Computes Initial Sum Efficiently**: Calculates the sum of the first `k` elements to start.  
- **Optimizes by Sliding the Window**: Updates the sum by adding the next element and removing the first element of the previous window.  
- **Runs in O(n) Time Complexity**: Traverses the array once, making it efficient for large inputs.  

<h4>Longest Repeating Character Replacement</h4>
<p>
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
</p>

<b>Solution Explanation:</b>
- **Uses Sliding Window Technique**: Expands the right pointer (`r`) while adjusting the left pointer (`l`) to maintain a valid substring.  
- **Tracks Character Frequency**: Stores character counts in a dictionary (`count`) to determine the most frequent character.  
- **Ensures Valid Window with At Most `k` Replacements**: Shrinks the window when the number of replacements exceeds `k`.  
- **Optimized O(n) Solution**: Each character is processed at most twice, making it efficient for large inputs.  

<h4>Permutation in String</h4>
<p>
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
</p>

<b>Solution Explanation</b>
- **Uses Frequency Counting for Character Comparison**: Maintains character counts for `s1` and a sliding window in `s2` using two arrays of size 26 (for lowercase letters).  
- **Initializes Counts for the First Window**: Computes character frequencies for the first `len(s1)` characters in `s2` to compare against `s1`.  
- **Sliding Window Optimization**: Updates character counts dynamically by adding the new character from the right (`r`) and removing the leftmost character (`l`).  
- **Efficient O(n) Approach**: Avoids unnecessary recomputation, ensuring optimal performance for checking permutations.