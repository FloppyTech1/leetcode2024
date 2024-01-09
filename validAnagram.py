# Key Idea
# Create two dictionaries, append each character to it's dictionary and increment it's value by one each time it appears. Compare both dictionaries, if they are equivalent,
# return true.

class Solution(object):
    def isAnagram(self, s, t):
        word1 = {} # Create dictionaries
        word2 = {}

        if len(s) != len(t): # If the lengths of the words are different, they cannot be anagrams.
            return False

        for char in range(len(s)): # Loop over the first word and append the characters to the dictionary.
            if s[char] in word1:
                word1[s[char]] += 1
            else:
                word1[s[char]] = 1
        
        for char in range(len(s)): # Loop over the second word and append the characters to the dictionary.
            if t[char] in word2:
                word2[t[char]] += 1
            else:
                word2[t[char]] = 1
        
        if word1 == word2: # Compare both dictionaries and return true or false.
            return True
        else:
            return False
