class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        left = 0
        right = n-1
        skill.sort()
        team_skill = skill[left] + skill[right]
        team_chem = skill[left] * skill[right]
        left += 1
        right -= 1
       
        while left < right:
            if skill[left] + skill[right] == team_skill:
                team_chem += skill[left] * skill[right]
                left += 1
                right -= 1       
            else:
                return -1
        
        return team_chem
        
