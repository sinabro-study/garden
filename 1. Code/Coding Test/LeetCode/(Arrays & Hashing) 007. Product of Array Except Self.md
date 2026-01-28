## Link

```cardlink
url: https://leetcode.com/problems/product-of-array-except-self/description/?q=Products+of+Array+Except+Self
title: "Product of Array Except Self - LeetCode"
description: "Can you solve this real interview question? Product of Array Except Self - Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.You must write an algorithm that runs in O(n) time and without using the division operation. Example 1:Input: nums = [1,2,3,4]Output: [24,12,8,6]Example 2:Input: nums = [-1,1,0,-3,3]Output: [0,0,9,0,0] Constraints: * 2 <= nums.length <= 105 * -30 <= nums[i] <= 30 * The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer. Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)"
host: leetcode.com
image: https://leetcode.com/static/images/LeetCode_Sharing.png
```

## Problems

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

## Example

**Input:** nums = `[1,2,3,4]`
**Output:** `[24,12,8,6]`

**Input:** nums = `[-1,1,0,-3,3]`
**Output:** [0,0,9,0,0]

## Constrains

- 2 <= `nums.length` <= $10^5$
- -30 <= `nums[i]` <= 30

## Solution

```python
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        # 왼쪽부터 차례대로 벽돌 쌓기
        mul = 1
        for i in range(1, length):
            result[i] = nums[i - 1] * mul
            mul *= nums[i - 1]

        # 오른쪽부터 차례대로 벽돌 쌓기
        mul = 1
        for i in range(length - 2, -1, -1):
            mul *= nums[i + 1]
            result[i] = result[i] * mul
        
        return result
```

## Result

![[Screenshot 2026-01-28 at 8.41.22 PM.png]]

## Description

- 왼쪽부터 자신을 제외하고 차례대로 쌓는다.
- 오른쪽부터 자신을 제외하고 차례대로 쌓는다.
- 둘의 곱은 자신을 제외한 모든 수의 곱으로 나타낼 수 있다.


![[Screenshot 2026-01-28 at 8.55.45 PM.png]]