'''''

Given two strings s and t, return true if t is an anagram of s, and false otherwise.


Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

'''''

# Can use a dictionary to check if letters are identical

class Solution:
    def createDict(self, s: str) -> dict:
        s_dict = {}
        for letter in s:
            if(letter in s_dict):
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        return s_dict

    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.createDict(s)
        t_dict = self.createDict(t)

        return s_dict == t_dict