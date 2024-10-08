# Generated by Django 5.0.7 on 2024-09-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('phone', models.BigIntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('disctption', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('counted_view', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('published_date', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': ' تیکت  ',
                'verbose_name_plural': 'تیکت ها   ',
                'ordering': ['created_date'],
            },
        ),
    ]
