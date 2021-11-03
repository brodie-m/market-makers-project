from django.db import models
import random
from pricing import price

# Create your models here.
class ETF(models.Model):
    ticker = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=2)
    previous_price = models.DecimalField(max_digits=2)
    sigma = models.IntegerField()
    

    def update_price(self):
        self.previous_price = self.current_price
        new_price = price(self.current_price,self.sigma,1,1)
        self.current_price = new_price

        
print(type(ETF))