from time import sleep
from django.db import models
import matplotlib.pyplot as plt
import numpy as np
import random


# Create your models here.


class ETF(models.Model):
    ticker = models.CharField(max_length=100)
    current_price = models.FloatField()
    previous_price = models.FloatField()
    sigma = models.DecimalField(decimal_places=3, max_digits=5)
    all_prices = models.CharField(max_length=100000)
    

    def price(self, initial_price, timestep, count):
        if initial_price <= 0:
            return
        if count < 1:
            return
        difference = (-1)**np.round(np.random.rand())*(np.random.rand() + np.random.rand()*timestep**(0.5))
        newPrice = initial_price + difference
        return newPrice
    
    def update_price(self):
        self.all_prices += f'{self.current_price},'
        self.previous_price = self.current_price
        new_price = self.price(self.current_price, 1, 1)
        self.current_price = new_price


