from models import ETF

from time import sleep

etfs = ETF.objects.all()

while True:
    sleep(5)
    for etf in etfs:
        etf.update_price()



