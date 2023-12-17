from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell,maximum=0,1,0
        while sell < len(prices) :
            if prices[buy] < prices[sell] :
                profit = prices[sell]-prices[buy]
                maximum =max(profit,maximum) 
            else:
                buy=sell
            sell+=1
        return maximum
    
