
```cardlink
url: https://leetcode.com/problems/two-sum/?q=two+sum
title: "Two Sum - LeetCode"
description: "Can you solve this real interview question? Two Sum - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order. Example 1:Input: nums = [2,7,11,15], target = 9Output: [0,1]Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].Example 2:Input: nums = [3,2,4], target = 6Output: [1,2]Example 3:Input: nums = [3,3], target = 6Output: [0,1] Constraints: * 2 <= nums.length <= 104 * -109 <= nums[i] <= 109 * -109 <= target <= 109 * Only one valid answer exists. Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?"
host: leetcode.com
image: https://leetcode.com/static/images/LeetCode_Sharing.png
```


## Problems

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

## Example

**Input:** nums = `[2,7,11,15]`, target = 9
**Output:** `[0,1]`
**Explanation:** `Because nums[0] + nums[1] == 9, we return [0, 1].`

## Constraints

- 2 <= `nums.length` <= $10^4$
- $-10^9$ <= `nums[i]` <= $10^9$
- -$10^9$ <= `target` <= $10^9$

## Solution

```python
# Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
           for j in range(i + 1, len(nums)):
              if nums[i] + nums[j] == target:
                 return [i, j]
                 
# Solution 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
           otherTager = target - nums[i]

           if otherTager in dic:
              return [dic[otherTager], i]
           dic[nums[i]] = i

        return []
```


## Result

![[Screenshot 2026-01-24 at 4.25.19 PM.png]]

![[Screenshot 2026-01-24 at 4.26.05 PM.png]]

## Description

#### Solution 1
`for loop문을 2번 사용`하면서 O($n^2$) 시간 복잡도를 가짐

#### Solution 2
`for loop문을 1회 사용`하면서 O($n$) 시간 복잡도로 수행함
python dictionary는 Hash Table로 구성되어 in 연산자 수행 시 O($1$)의 시간 복잡도를 가짐
