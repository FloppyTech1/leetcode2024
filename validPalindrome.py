# Key idea
# Convert to lowercase, remove all special characters, reverse the string and compare both. Return the result.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]+', '', s)
        rev = s[::-1]

        return s == rev
