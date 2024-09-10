# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert string to list to allow in-place modifications
        s = list(s)  # {{ edit_1 }}
        
        # Function to reverse a portion of the list
        def reverse_range(start, end):  # {{ edit_2 }}
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        # Reverse the entire list
        reverse_range(0, len(s) - 1)  # {{ edit_3 }}
        
        # Reverse each word in the list
        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                reverse_range(start, end - 1)  # {{ edit_4 }}
                start = end + 1
        reverse_range(start, len(s) - 1)  # Reverse the last word
        
        # Join the characters and filter out extra spaces
        return ' '.join(''.join(s).split())  # {{ edit_5 }}
