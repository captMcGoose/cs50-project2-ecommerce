# Generated by Django 3.2.5 on 2021-09-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='img_url',
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=999),
        ),
    ]