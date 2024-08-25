'''The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.'''


# Version 1: iterative solution

class Solution:
    def countAndSay(self, n: int) -> str:
        def map_int_to_sequence(num: str):
            res = []
            curr = []
            curr_total = 0
            num = str(num)
            curr_char = num[0]

            for char in num:
                if char == curr_char:
                    curr_total += 1

                else:
                    curr.append(curr_char)
                    curr.append(curr_total)
                    res.append(curr)
                    curr_char, curr_total = char, 1
                    curr = []

            curr.append(curr_char)
            curr.append(curr_total)
            res.append(curr)
            return res

        def map_sequence_to_int(arr: list):
            res = ''

            for digit, count in arr:
                res += str(count) + digit

            return res

        current = "1"
        for _ in range(n - 1):
            pairs = map_int_to_sequence(current)
            current = map_sequence_to_int(pairs)

        return current


# Version 2: recursive

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        previous_seq = self.countAndSay(n - 1)

        res = ""
        i = 0
        while i < len(previous_seq):
            count = 1
            while i + 1 < len(previous_seq) and previous_seq[i] == previous_seq[i + 1]:
                i += 1
                count += 1
            res += str(count) + previous_seq[i]
            i += 1

        return res
