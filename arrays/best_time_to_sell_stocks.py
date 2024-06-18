from typing import List

'''You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        score = 0
        curr_bought = None
        curr_max = 0

        for i in range(len(prices)):

            # handle last idx
            if i == len(prices) - 1:
                if curr_bought is not None:
                    if curr_max < prices[i]:
                        score += prices[i] - curr_bought
                    else:
                        score += curr_max - curr_bought
                break

            # buy
            if curr_bought is None and prices[i] < prices[i+1]:
                curr_bought = prices[i]
                curr_max = prices[i+1]
                continue

            # change max
            if curr_bought is not None and curr_max < prices[i+1]:
                curr_max = prices[i+1]
                continue

            # sell
            if curr_bought is not None and curr_max > prices[i+1]:
                score += curr_max - curr_bought
                curr_bought, curr_max = None, 0

                
        return score
