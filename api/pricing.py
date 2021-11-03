import random
# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from pandas.plotting import register_matplotlib_converters
# register_matplotlib_converters()
prices=[]
def price(initial, sigma, timestep, count):
    if initial <= 0:
        return
    if count < 1:
        return
    # prices.append(initial)
    difference = (-1)**(np.round(np.random.rand()))*(np.random.rand()*sigma*timestep + np.random.rand()*timestep**(0.5) )
    newPrice = initial + difference
    return price(newPrice,sigma,timestep,count-1)
#
# 
# 
#  price(5,1,0.1,500)
# # print(prices)
# days = []
# for i in range(0,len(prices)):
#     days.append(i)
# plt.plot(days,prices)
# plt.show()
