## Link

```cardlink
url: https://leetcode.com/problems/encode-and-decode-strings/description/
title: "Encode and Decode Strings - LeetCode"
description: "Can you solve this real interview question? Encode and Decode Strings - Level up your coding skills and quickly land a job. This is the best place to expand your knowledge and get prepared for your next interview."
host: leetcode.com
image: https://leetcode.com/static/images/LeetCode_Sharing.png
```

## Problems

Design an algorithm to encode **a list of strings** to **a string**. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

```text
string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
```

Machine 2 (receiver) has the function:

```text
vector<string> decode(string s) {
    //... your code
    return strs;
}
```

So Machine 1 does:

```text
string encoded_string = encode(strs);
```

and Machine 2 does:

```text
vector<string> strs2 = decode(encoded_string);
```

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

## Example

```java
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
```

```java
Input: dummy_input = [""]
Output: [""]
```

## Constrains

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains any possible characters out of `256` valid ASCII characters.

## Solution

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = ':'.join([str(len(x)) for x in strs])
        content = ''.join(strs)

        return f'{lengths}#{content}'

    def decode(self, s: str) -> List[str]:
        nums, texts = s.split('#', 1)

        if not nums:
            return []

        nums = list(map(int, nums.split(":")))        
        result = []

        for num in nums:
            if not num:
                result.append("")
                continue

            result.append(texts[:num])
            texts = texts[num:]
        
        return result
```

## Result

![[Screenshot 2026-01-27 at 9.37.56 PM.png]]

## Description

- 256 ASCII 코드가 문자열이 될 수 있기 때문에 어떤 문자열을 추가한다하더라도 구분자로 사용할 수 없다.
- 인코딩 시 임의의 구분자를 사용하여 문자열 길이의 집합과 문자열 집합을 구분할 수 있도록 해야한다.

- 인코딩
	- 각 문자열 별 길이와 문자열을 결합한다.
	- 각 문자열의 길이를 구분할 수 있도록 구분자를 추가한다.
- 디코딩
	- 문자열의 길이들과 문자열을 나눈다.
	- 문자열의 길이들도 구분자로 나눈다.
	- 문자열을 각 문자열의 길이로 나눈다.
	- 단, 문자열의 길이가 없는 경우 (즉, 인코딩 시 빈 값인 경우) 빈 배열을 반환해야한다.
