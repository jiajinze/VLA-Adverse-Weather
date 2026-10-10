# LeetCode 刷题记录

> 每天1题，3年见证改变。

## 📊 进度

- **开始日期**: 2026-10-10
- **目标**: 校招前 500题
- **当前**: 0 题

## 📁 文件命名规则

`YYYY-MM-DD_题号_题目.py`

例：`2026-10-10_001_two_sum.py`

## 📚 题目模板

```python
"""
题目: 1. Two Sum 两数之和
链接: https://leetcode.cn/problems/two-sum/
难度: Easy
日期: 2026-10-10
用时: 30 min

题目描述:
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。

示例:
输入: nums = [2, 7, 11, 15], target = 9
输出: [0, 1]

思路:
1. 暴力法：双重循环 O(n²)
2. Hash表法：一次遍历 O(n) 空间换时间

时间复杂度: O(n)
空间复杂度: O(n)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []
```

## 📁 文件结构

```
leetcode/
├── README.md
├── notes/             # 笔记
│   ├── 2026-10-10.md
│   └── ...
├── solutions/         # 解法
│   ├── 2026-10/
│   │   ├── 001_two_sum.py
│   │   └── ...
│   └── ...
```

## 题目列表

### 2026-10
- 10.10: [001 Two Sum](./solutions/2026-10/001_two_sum.py) - E
