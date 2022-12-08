class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ## FIND THE SHORTEST WORD IN THE LIST

        lengths = [] # to keep track of each word length
        start   = '' # the shortest word
        
        for word in strs:
            lengths.append(len(word))          
            if len(word) == min(lengths):
                start = word

        l     = len(start) # length of the shortest word
        check = 0          # to keep track of the common prefixes


       
       ## USE THIS WORD TO FIND THE LONGEST COMMON PREFIX
       ## REMOVE A LETTER FROM THE END OF THIS WORD FOR EACH ROUND

        while check != len(strs): 
            for i in range(len(strs)):
                if strs[i][:l] == start:
                    check += 1 
                    # if the prefix of the word matches start, add 1 to "check", otherwise leave as is
                
            # if all of the words in the list match start, return the longest common prefix
            # (if there isn't one, return an empty string)
            if check == len(strs): # (for all to match, check must equal the number of words in the list)
                return start
            
            # repeat as long as check != len(strs). 
            # each time, remove one letter from the end of start, and reset "check"    
            l -= 1
            start = start[:l]
            check = 0
