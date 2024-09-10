# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'  # String of vowels
        s_list = list(s)  # Convert string to list for mutability
        left, right = 0, len(s) - 1  # Two pointers

        while left < right:
            # Move left pointer to the next vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move right pointer to the previous vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # Swap the vowels
            if left < right:  # Only swap if pointers haven't crossed
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        return ''.join(s_list)  # Convert list back to string


