# Generated by Django 3.2.9 on 2021-11-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ETF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=100)),
                ('current_price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('previous_price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('sigma', models.DecimalField(decimal_places=3, max_digits=5)),
                ('all_prices', models.CharField(max_length=100000)),
            ],
        ),
    ]
