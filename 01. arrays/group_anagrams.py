'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''


class Solution:
    def groupAnagrams(self, strs):
        anagrams_dict = {}

        for word in strs:
            sorted_chars = ''.join(sorted(word))
            key_to_add = anagrams_dict.get(sorted_chars)

            if not key_to_add:
                anagrams_dict[sorted_chars] = [word]

            else:
                anagrams_dict[sorted_chars].append(word)

        res = [v for v in anagrams_dict.values()]
        return res
