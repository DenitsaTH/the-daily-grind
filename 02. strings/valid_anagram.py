'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    dict_s, dict_t = {}, {}

    for i in range(len(s)):
        dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
        dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

    for k in dict_s:
        if dict_s[k] != dict_t.get(k, 0):
            return False

    return True


print(isAnagram('anagram', 'nagaram'))
