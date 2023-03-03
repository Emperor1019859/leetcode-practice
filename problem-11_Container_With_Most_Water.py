"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
[ref_pic]("https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg")
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from statistics import mean
from math import ceil


class Solution:  # TODO: strongly need refactor
    def maxArea(self, height: list[int]) -> int:
        if len(height) == 2:
            return min(height)

        max_area, largest = min(height), mean(height) - 1
        for index, cur_height in enumerate(height):
            if cur_height > largest:
                largest = cur_height
                least_width = ceil(max_area / cur_height) if cur_height else 0

                possibility = range(0, len(height) - index - least_width)
                for extra_width in possibility:
                    width = least_width + extra_width
                    min_height = min(cur_height, height[index + width])
                    area = width * min_height

                    if area > max_area:
                        max_area = area

        return max_area


# Runtime 7229 ms Beats 5% Memory 27.5 MB Beats 45.84%
