class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # List[], Tuple(), Set{}, Dictionary{}: Collections

        #Anagram contains same charaacters on diff page
        if len(s) != len (t):
            return False
        
        change = {}
        seen = set()

        for i in range(len(s)):
            if s[i] in change:
                change[s[i]] += 1
            else:
                change[s[i]] = 1
                seen.add(s[i])
            
            if t[i] in change:
                change[t[i]] -= 1
            else:
                change[t[i]] = -1
                seen.add(t[i])
        for value in change.values():
            if value != 0:
                return False
        return True 
