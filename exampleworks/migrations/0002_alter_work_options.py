# Generated by Django 5.0.7 on 2024-09-15 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exampleworks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['created_date'], 'verbose_name': 'نمونه کار', 'verbose_name_plural': ' نمونه کار ها '},
        ),
    ]
