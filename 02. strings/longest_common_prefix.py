'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".'''


def longestCommonPrefix(strs) -> str:

    curr_idx = 0
    chars = []

    while curr_idx < len(strs[0]):
        curr_char = strs[0][curr_idx]

        for i in range(1, len(strs)):

            if curr_idx >= len(strs[i]) or strs[i][curr_idx] != curr_char:
                return '' if not chars else ''.join(chars)

        chars.append(curr_char)
        curr_idx += 1

    return '' if not chars else ''.join(chars)
