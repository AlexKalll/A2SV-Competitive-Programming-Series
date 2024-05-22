class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        l = 0
        counts, countp = {}, {}
        res = []
        
        for i in range(len(p)):
            countp[p[i]] = 1 + countp.get(p[i], 0)
            counts[s[i]] = 1 + counts.get(s[i], 0)
        res=[0] if countp == counts  else  []

        for r in range(len(p), len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            counts[s[l]] -= 1

            if counts[s[l]] == 0:
                counts.pop(s[l])
            l += 1
            if countp == counts:
                res.append(l)
        return res
