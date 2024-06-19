from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            
        else:
            for num in range(len(digits) - 1, -1, -1):
                if digits[num] == 9:
                    digits[num] = 0
                else:
                    digits[num] += 1
                    break
            else:
                digits.insert(0, 1)
                
        return digits
