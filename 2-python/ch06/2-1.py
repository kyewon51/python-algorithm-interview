from typing import List
name = "BlockDMask"
reverse_name = ''

for c in name:
    reverse_name = c + reverse_name

print(f'name    : {name}')
print(f'reverse : {reverse_name}')
출처: https://blockdmask.tistory.com/581 [개발자 지망생:티스토리]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
