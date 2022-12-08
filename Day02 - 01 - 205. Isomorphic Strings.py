# 205. Isomorphic Strings
# Time taken: 53 m 51 s

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        mapping = {}
        i=0
        
        # 1. create a dictionary with the mapping (letters in t=key,s=value)
        for letter in s:
            if letter not in mapping.values():
                mapping.update({t[i]:letter})
            i+=1
        
        word = []

        # 2. use the mapping to generate a word from the letters of t
        for letter in t:
            word.append(mapping.get(letter))
            # dict.get(...) returns None if the key doesn't exist in the dictionary
        
        # 3. check if this word equals s
        if ''.join(letter for letter in word if letter) == s:
            return True
        else:
            return False
            
            
