'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    
        if len(needle) > len(haystack):
            return -1

        curr_haystack, curr_needle = 0, 0
        start = None
        has_match = False

        while curr_haystack < len(haystack):
            
            for i in range(curr_haystack, len(haystack)):
                for j in range(curr_needle, len(needle)):

                    if haystack[i] == needle[j]:
                        if start is None:
                            start = i
                        has_match = True
                        break
                    
                    else:
                        has_match = False
                        break

                if has_match:
                    curr_needle += 1
                    if curr_needle > len(needle):
                        return start
                    continue

                else:
                    curr_haystack += 1
                    start, curr_needle = None, 0
                    break

        return -1
