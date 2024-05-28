class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        n = len(tickets)
        queue = deque([(i, tickets[i]) for i in range(n)])
        time = 0

        while queue:
            i, count = queue.popleft()
            if count > 1:
                queue.append((i, count - 1))
            elif i == k and count == 1:
                return time + 1
            else:
                time += 1

        return time
