# Generated by Django 5.1.5 on 2025-02-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='vriations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
