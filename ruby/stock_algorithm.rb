# stock_algorithm.rb

# I have an array stock_prices_yesterday where:

# The indices are the time, as a number of minutes past trade opening time, which was 9:30am local time.
# The values are the price of Apple stock at that time, in dollars.
# For example, the stock cost $500 at 10:30am, so stock_prices_yesterday[60] = 500.

# Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday. For this problem, we won't allow "shorting"—you must buy before you sell.

# brute-force pseudo code:
# 1. enumerate all buy, sell pairs
# 2. keep track of the largest difference
# 3. return difference

stock_prices_yesterday = [3,3,4,5,3,1,5,6,8,9,4,12,11,10,14,14,14,18,15]

def best_profit_from_yesterday(prices_array)
  best_profit = 0
  prices_array.each_with_index do |potential_buy_price,index|
    for potential_sell_index in index..prices_array.length-1

      immediate_profit = prices_array[potential_sell_index] - potential_buy_price
      if immediate_profit > best_profit
        best_profit = immediate_profit
      end
    end
  end
  p "best_profit #{best_profit}"
  best_profit
end
p best_profit_from_yesterday(stock_prices_yesterday)

# brute-force analysis:
# time: O(n^2) due to two nested loops
# space: O(1) constant, no new arrays created just a constant amount of variables

#Greedy Approach - We can get time complexity to O(n)
#Pseudocode:
# 1. Keep lowest price seen so far
# 2. Keep max profit
# 3. Check if sellling at each point and buying at lowest so far is greater than max profit so far

def best_profit_from_yesterday_greedy(prices_array)

  lowest_thus_far = prices_array[0]
  max_profit = 0

  prices_array.each do |price|
    if price < lowest_thus_far
      lowest_thus_far = price
    end

    potential_profit = price - lowest_thus_far
    if(potential_profit > max_profit)
      max_profit = potential_profit
    end
  end
  max_profit
end

p best_profit_from_yesterday_greedy(stock_prices_yesterday)

#greedy analysis:
# 1. O(n) time!! Only one pass thru the array
# 2. O(1) space still only a constant number of variables

#Notes from solution:
# use more ruby helper functions instead of if's i.e. lowest_thus_far = min(lowest_thus_far, current_price)
# max_profit = max(max_profit, current_price - lowest_thus_far)
