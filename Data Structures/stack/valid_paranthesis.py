'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''
class Solution:
    def isValid(self, s: str) -> bool:
        map_data = {'(':')', '{':'}', '[':']'}
        flag = True
        if len(s) % 2 != 0:
            return False

        stack = []
        for char in s:
            if char in map_data.keys():
                stack.append(char)
            elif stack:
                last_elem = stack.pop()
                if map_data[last_elem] != char:
                    flag = False
                    break
            else:
                flag = False
        if stack:
            flag = False

        return flag
