"""238. Product of Array Except Self #Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from functools import reduce
import operator


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        total_product_v = reduce(operator.mul, nums)

        for idx, value in enumerate(nums):
            # if total_product_v and value both 0, p_v might not be 0
            if total_product_v == 0 and value == 0:
                temp = value
                nums[idx] = 1
                p_v = reduce(operator.mul, nums)
                nums[idx] = temp
            else:
                p_v = int(total_product_v / value) if value else 0

            result.append(p_v)

        return result


# Runtime 266 ms Beats 66.57%
# Memory 25.78 MB Beats 49.14%
