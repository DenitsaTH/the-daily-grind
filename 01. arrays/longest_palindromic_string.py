'''Given a string s, return the longest palindromic substring in s.'''


# Version 1: generate all possible substrings -> O(n3) time complexity

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        palindromes = []
        max = 0

        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    t = (s[i:j], len(s[i:j]))
                    if max < len(s[i:j]):
                        palindromes.append(t)
                        max = len(s[i:j])

        palindromes.sort(key=lambda x: x[1], reverse=True)
        return palindromes[0][0]


# Version 2: optimized -> expand around the center -> O(n2) time complexity

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""

        for i in range(len(s)):
            odd_palindrome = expand_around_center(i, i)
            even_palindrome = expand_around_center(i, i + 1)

            longest_palindrome = max(
                longest_palindrome, odd_palindrome, even_palindrome, key=len)

        return longest_palindrome
