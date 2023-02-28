"""
The count-and-say sequence is str_num sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
which is then converted into str_num different digit string.

To determine how you "say" str_num digit string,
split it into the minimal number of substrings such that each substring
contains exactly one unique digit. Then for each substring,
say the number of digits, then say the digit.
Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

Given str_num positive integer n, return the nth term of the count-and-say sequence.

Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Constraints:

1 <= n <= 30
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"

        return self.say(self.countAndSay(n - 1))

    @staticmethod
    def say(str_num: str) -> str:
        result = ""
        count = 1

        for index in range(len(str_num) - 1):
            if str_num[index + 1] == str_num[index]:
                count += 1
            else:
                result += f"{count}{str_num[index]}"
                count = 1

        # handle last element
        if str_num[-1] != str_num[-2]:
            result += f"1{str_num[-1]}"
        else:
            result += f"{count}{str_num[-2]}"

        return result


# Runtime 30 ms Beats 99.77% Memory 13.9 MB Beats 48.11%
