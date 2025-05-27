from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lista = []

        for i in accounts:
            lista.append(sum(i))
        return max(lista)
