class Solution:
    def isPalindrome(self, s: str) -> bool:
        updatedstr = "".join(char.lower() for char in s if char.isalnum())
        return updatedstr  == updatedstr[::-1]
        