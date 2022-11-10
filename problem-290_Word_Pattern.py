"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(" ")):
            return False

        pattern_dict = {}
        for key, word in zip(pattern, s.split(" ")):
            if not pattern_dict.get(key):
                if word in pattern_dict.values():
                    return False
                pattern_dict[key] = word
            elif pattern_dict.get(key) != word:
                return False

        return True


sol = Solution()
pattern = "abba"
s = "cat dog dog cat"
result = sol.wordPattern(pattern, s)
print(result)

# Runtime 37 ms Beats 84.46% Memory 13.8 MB Beats 75.28%
