'''Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.'''


class Solution:
    def firstUniqChar(self, s: str) -> int:

        vals_count = {}

        for i in range(len(s)):

            if s[i] not in vals_count:
                vals_count[s[i]] = i
            else:
                vals_count[s[i]] = None

        for v in vals_count.values():
            if v is not None:
                return v

        return -1
