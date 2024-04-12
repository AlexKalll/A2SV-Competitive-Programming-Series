class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = {}
        losses = {}
        for match in matches:        
            wins[match[0]] = wins.get(match[0], 0) + 1
            losses[match[1]] = losses.get(match[1], 0) + 1

        no_losses = [player for player in wins if player not in losses]
        players_with_1_loss = [player for player, count in losses.items() if count == 1]
        no_losses.sort()
        players_with_1_loss.sort()
        return [no_losses, players_with_1_loss]
