
```cardlink
url: https://leetcode.com/problems/valid-anagram/description/?q=Valid+Anagram
title: "Valid Anagram - LeetCode"
description: "Can you solve this real interview question? Valid Anagram - Given two strings s and t, return true if t is an anagram of s, and false otherwise. Example 1:Input: s = \"anagram\", t = \"nagaram\"Output: trueExample 2:Input: s = \"rat\", t = \"car\"Output: false Constraints: * 1 <= s.length, t.length <= 5 * 104 * s and t consist of lowercase English letters. Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"
host: leetcode.com
image: https://leetcode.com/static/images/LeetCode_Sharing.png
```

## Problems

Given two strings `s` and `t`, return `true` if `t` is an anagram[^1] of `s`, and `false` otherwise.

## Example

**Input:** s = "anagram", t = "nagaram"
**Output:** true

## Contraints

- 1 <= s.length, t.length <= 5 * $10^4$
- `s` and `t` consist of lowercase English letters.

## Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       source = [0] * 26
       target = [0] * 26

       for alpha in s:
          source[ord(alpha) - ord('a')] += 1

       for alpha in t:
          target[ord(alpha) - ord('a')] += 1

       return source == target
```



## Result

![[Screenshot 2026-01-24 at 3.56.07 PM.png]]




[^1]: An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once
