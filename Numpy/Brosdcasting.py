# prices = [100, 200, 300]

# discount = 10

# final_prices = []

# for i in prices:
#   final_price = i - (i * 0.1)
#   final_prices.append(final_price)

# print(final_prices) 

'''
This is a problem statment, in case of large datasets, using loops is 
expensive when it comes to time so to counter that we have used the following 
'''

import numpy as np

prices = np.array([100, 200, 300])
print("Prices :", prices)

final_prices = prices - (prices * 0.1)
print("After Discount prices :", final_prices)