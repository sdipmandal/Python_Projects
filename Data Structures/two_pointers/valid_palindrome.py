"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # word_string = "".join([x.lower() for x in s if x.isalnum()])
        # reverse_word = "".join([x for x in word_string[-1::-1]])
        # print(word_string)
        # print(reverse_word)
        # return word_string == reverse_word
        cursor1, cursor2 = "", ""
        for i, alph in enumerate(s):
            if alph.isalnum():
                cursor1 = alph.lower()
            
            if s[len(alph)-i].isalnum():
                cursor2 = s[len(alph)-i].lower()

            if cursor1 and cursor2:
                if cursor1 == cursor2:
                    cursor1, cursor2 = "", ""
                    continue
                else:
                    return False
            else:
                continue


sol = Solution()
print(sol.isPalindrome('A man, a plan, a canal: Panama'))