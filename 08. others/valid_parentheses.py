'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets_mapping.values():
                stack.append(char)
            elif char in brackets_mapping:
                if stack and stack[-1] == brackets_mapping[char]:
                    stack.pop()
                else:
                    return False

        return not stack
