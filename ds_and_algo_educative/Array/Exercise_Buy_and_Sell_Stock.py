

'''Given an array of numbers consisting of daily stock prices,
 calculate the maximum amount of profit that can be made from buying on one day and selling on another.
In an array of prices, each index represents a day,
and the value on that index represents the price of the stocks on that day.
Note that you need to buy the stocks before you sell them
 so the day (index) indicating the buying price should be before the day (index) indicating the selling price.
'''

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def buy_and_sell_once(A):
  max_profit = 0
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[j] - A[i] > max_profit:
          max_profit = A[j] - A[i]
  return max_profit

print(buy_and_sell_once(A))