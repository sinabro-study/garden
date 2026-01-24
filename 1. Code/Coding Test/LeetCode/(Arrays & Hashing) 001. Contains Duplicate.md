
```cardlink
url: https://leetcode.com/problems/contains-duplicate/description/
title: "Contains Duplicate - LeetCode"
description: "Can you solve this real interview question? Contains Duplicate - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. Example 1:Input: nums = [1,2,3,1]Output: trueExplanation:The element 1 occurs at the indices 0 and 3.Example 2:Input: nums = [1,2,3,4]Output: falseExplanation:All elements are distinct.Example 3:Input: nums = [1,1,1,3,3,4,3,2,4,2]Output: true Constraints: * 1 <= nums.length <= 105 * -109 <= nums[i] <= 109"
host: leetcode.com
image: https://leetcode.com/static/images/LeetCode_Sharing.png
```


## Problems

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Example

**Input:** nums = [1, 2, 3, 1]
**Output:** true
**Explanation:**
The element 1 occurs at the indices 0 and 3.

## Solution

```python
from typing import List


class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
  
if __name__ == "__main__":
  solution = Solution()
  print(solution.containsDuplicate([1, 2, 3, 1]))
```

## Result
![[Screenshot 2026-01-24 at 11.21.29 AM.png]]

