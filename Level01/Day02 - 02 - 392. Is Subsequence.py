# 392. Is Subsequence
# Time taken: 39 m 30 s + ~ 1.5 hours

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        word = t
        res = 0

        for letter in t:
            if letter not in s:
                word = word.replace(letter,"")
        
        for letter in s:
            if letter in word and len(s) <= len(word) and (s in word or s.index(letter) <= word.index(letter)):
                res += 1

        return res == len(s)
        
        '''
        examples
        --------------------
        letter in word::: s = ab, t = baab
        len(s) <= len(word)::: s = aaaaa, t = bbaaa
        (s in word or s.index(letter) <= word.index(letter))::: s=leeeeetcode (5 e's), word=leeeeeetcode (5 e's) - with t being lyyyyeyyyyeyyyyeyyyyeyyyeyyytcode - bunch of y's inbetween
        
        '''