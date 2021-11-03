from rest_framework import serializers
from .models import ETF

class ETFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ETF
        fields = ('ticker','current_price','previous_price','sigma','all_prices')
