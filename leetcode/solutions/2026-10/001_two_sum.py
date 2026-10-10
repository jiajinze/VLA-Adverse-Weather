"""
题目: 1. Two Sum 两数之和
链接: https://leetcode.cn/problems/two-sum/
难度: Easy
日期: 2026-10-10

题目描述:
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。

示例:
输入: nums = [2, 7, 11, 15], target = 9
输出: [0, 1]
解释: 因为 nums[0] + nums[1] = 2 + 7 = 9

思路演进:
1. 暴力法：双重循环 O(n²)
2. Hash表：一次遍历 O(n)，空间换时间

时间复杂度: O(n)
空间复杂度: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Hash表法：边遍历边查"配对"
        """
        hash_map = {}  # 值 -> 下标
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []  # 题目保证有解，这里其实不会执行


# 测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))       # [1, 2]
    print(sol.twoSum([3, 3], 6))          # [0, 1]
