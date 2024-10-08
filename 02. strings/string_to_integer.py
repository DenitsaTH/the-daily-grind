'''Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").

Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.

Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. 
If no digits were read, then the result is 0.

Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. 
Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.'''


# ----------- Version 1 -----------

class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        start, end = None, None
        sign = 1

        s = s.strip()

        for i in range(len(s)):
            if i == 0 and s[i] == '+':
                continue

            if i == 0 and s[i] == '-':
                sign = -1
                continue

            if not s[i].isdigit():
                break

            else:
                if start is None:
                    start = i
                else:
                    end = i

        if start is None:
            return 0
        if end is None:
            return int(s[start]) * sign

        res = int(s[start:end+1]) * sign

        if res < INT_MIN:
            res = INT_MIN
        if res > INT_MAX:
            res = INT_MAX

        return res


# ----------- Version 2 -----------

class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        s = s.strip()
        if not s:
            return 0

        sign = 1
        i = 0
        if s[0] == '+':
            i += 1
        elif s[0] == '-':
            sign = -1
            i += 1

        num = 0

        for idx in range(i, len(s)):

            if not s[idx].isdigit():
                break

            num = num * 10 + int(s[idx])

        res = sign * num

        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX

        return res
