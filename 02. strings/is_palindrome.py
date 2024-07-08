import re

'''Given a string s, return true if it is a palindrome, or false otherwise.'''


class Solution:

    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^a-zA-Z0-9]+'
        new_s = re.sub(pattern, '', s).lower()

        start_idx, end_idx = 0, len(new_s) - 1

        while start_idx < end_idx:
            if new_s[start_idx] != new_s[end_idx]:
                return False

            start_idx += 1
            end_idx -= 1

        return True
