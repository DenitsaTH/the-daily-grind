'''Given a roman numeral, convert it to an integer.'''


class Solution:
    def romanToInt(self, s: str) -> int:

        roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        def special_case(c1, c2):
            return (c1 == 'I' and c2 in ['V', 'X']) or \
                   (c1 == 'X' and c2 in ['L', 'C']) or \
                   (c1 == 'C' and c2 in ['D', 'M'])

        special_values = {
            'IV': 4, 'IX': 9,
            'XL': 40, 'XC': 90,
            'CD': 400, 'CM': 900
        }

        num = []
        c = 0  # counter

        while c < len(s):
            if c < len(s) - 1 and special_case(s[c], s[c + 1]):
                num.append(special_values[s[c] + s[c + 1]])
                c += 2
            else:
                num.append(roman_nums[s[c]])
                c += 1

        return sum(num)
