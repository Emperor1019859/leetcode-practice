"""
# Hard
Given an unsorted integer array nums.
Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        sorted_nums = sorted((n for n in nums if n > 0))
        if not sorted_nums:
            return 1

        smallest = 1
        for num in sorted_nums:
            if smallest < num:
                return smallest

            smallest = num + 1

        return smallest


nums = [4, 3, 4, 1, 1, 4, 1, 4]
result = Solution().firstMissingPositive(nums)
print(result)  # 2

# Runtime 364 ms Beats 14.30% of users with Python3
# Memory 30.27 MB Beats 80.75% of users with Python3
