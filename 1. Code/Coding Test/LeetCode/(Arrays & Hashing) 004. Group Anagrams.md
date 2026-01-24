
```cardlink
url: https://leetcode.com/problems/group-anagrams/description/?q=Group+Anagrams
title: "Group Anagrams - LeetCode"
description: "Can you solve this real interview question? Group Anagrams - Given an array of strings strs, group the anagrams together. You can return the answer in any order. Example 1:Input: strs = [\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]Output: [[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]Explanation: * There is no string in strs that can be rearranged to form \"bat\". * The strings \"nat\" and \"tan\" are anagrams as they can be rearranged to form each other. * The strings \"ate\", \"eat\", and \"tea\" are anagrams as they can be rearranged to form each other.Example 2:Input: strs = [\"\"]Output: [[\"\"]]Example 3:Input: strs = [\"a\"]Output: [[\"a\"]] Constraints: * 1 <= strs.length <= 104 * 0 <= strs[i].length <= 100 * strs[i] consists of lowercase English letters."
host: leetcode.com
image: https://leetcode.com/static/images/LeetCode_Sharing.png
```


## Problems

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

## Example

**Input:** strs = `["eat","tea","tan","ate","nat","bat"]`
**Output:** `[["bat"],["nat","tan"],["ate","eat","tea"]]`

## Constrains

- 1 <= `strs.length` <= $10^4$
- 0 <= `strs[i].length` <= 100
- `strs[i]` consists of lowercase English letters.

## Solution

```python
from typing import List
from collections import defaultdict

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for value in strs:
      key = ''.join(sorted(value))
      groups[key].append(value)

    return list(groups.values())
```

## Result

![[Screenshot 2026-01-24 at 6.14.39 PM.png]]

## Description

- 동일한 Anagram을 key 값으로 두어야 함.
	- 같은 값은 하나로 합쳐서 반환해야하기 때문에 list로 기본값 설정
	- Hash 값을 활용하여 탐색 속도를 O($1$)으로 하기 위함
