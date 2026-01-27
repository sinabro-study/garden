## Link

```cardlink
url: https://leetcode.com/problems/top-k-frequent-elements/description/?q=Top+K+Frequent+Elements
title: "Top K Frequent Elements - LeetCode"
description: "Can you solve this real interview question? Top K Frequent Elements - Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. Example 1:Input: nums = [1,1,1,2,2,3], k = 2Output: [1,2]Example 2:Input: nums = [1], k = 1Output: [1]Example 3:Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2Output: [1,2] Constraints: * 1 <= nums.length <= 105 * -104 <= nums[i] <= 104 * k is in the range [1, the number of unique elements in the array]. * It is guaranteed that the answer is unique. Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size."
host: leetcode.com
image: https://leetcode.com/static/images/LeetCode_Sharing.png
```

## Problems

Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.

## Example

**Input:** nums = `[1,1,1,2,2,3]`, k = 2
**Output:** `[1,2]`

## Constrains

- 1 <= nums.length <= $10^5$
- $-10^4$ <= nums[i] <= $10^4$
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

## Solution

```python
from typing import List
from collections import Counter
import heapq

# Solution 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        return sorted(x, key = x.get, reverse=True)[:k] 

# Solution 2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        return heapq.nlargest(k, x.keys(), key=x.get)
```

## Result

![[Screenshot 2026-01-24 at 6.28.13 PM.png]]

## Description

- 중복된 개수를 구해야하므로 Counter를 활용
- Solution 1
	- 시간 복잡도 O($N + MlogM$) 소요
		- Counter(nums): O($N$)
		- sorted 함수는 timesort 사용하므로: O($MlogM$)

- Solution 2
	- 시간 복잡도 O($N + NlogK$) 소요
		- heap을 사용하여 시간 복잡도 감소
		- 결과는 동일[^1]




[^1]: Find the n largest elements in a dataset. Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
