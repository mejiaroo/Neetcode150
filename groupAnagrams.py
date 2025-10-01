# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

class Solution:
    def createDict(self, s: str) -> dict:
        s_dict = {}
        for letter in s:
            if(letter in s_dict):
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        return s_dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = []
        for index, s in enumerate(strs):
            if(solution and any(s in sublist for sublist in solution)):
                continue
            curr = [s]
            sD = self.createDict(s)
            for index2, s2 in enumerate(strs):
                if(index2 == index):
                    continue
                s2D = self.createDict(s2)
                if s2D == sD:
                    curr.append(s2)
            solution.append(curr)
        return solution