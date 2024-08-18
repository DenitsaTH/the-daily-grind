/*Given a string s, find the length of the longest substring without repeating characters.*/

var lengthOfLongestSubstring = function (s) {
    let maxLen = 0;
    let ss = new Set();
    let left = 0;

    for (let right = 0; right < s.length; right++) {
        const currentChar = s[right];

        while (ss.has(currentChar)) {
            ss.delete(s[left]);
            left++;
        }

        ss.add(currentChar);

        const currLen = right - left + 1;
        if (currLen > maxLen) {
            maxLen = currLen;
        }
    }

    return maxLen;
};

console.log(lengthOfLongestSubstring("abcabcbb"));