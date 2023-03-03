"""
Given a string s, find the length of the longest substring without repeating characters.

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

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:  # TODO: need refactor
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for index in range(len(s)):
            count, current = 0, {}

            for char in s[index:]:
                if char in current:
                    break

                current[char] = 1
                count += 1

                if count > longest:
                    longest = count

        return longest


# Runtime 404 ms Beats 16.2% Memory 14 MB Beats 89.70% (2nd attempt)
