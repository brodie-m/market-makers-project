import random
# import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from pandas.plotting import register_matplotlib_converters
# register_matplotlib_converters()

prices=[]

def price(initial, sigma, timestep, count):
    if count < 1:
        return
    prices.append(initial)
    difference = (-1)**(np.floor(np.random.rand()))*(np.random.rand()*sigma*timestep + np.random.rand()*timestep**(0.5) )
    newPrice = initial + difference 
    
    return price(newPrice,sigma,timestep,count-1)

price(5,1,1,50)
print(prices)