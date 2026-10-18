class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        supdated = "".join(char.lower() for char in s if char.isalnum())
        tupdated = "".join(char.lower() for char in t if char.isalnum())

        return sorted(supdated) == sorted(tupdated)
         
        