# Generated by Django 5.0.7 on 2024-09-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('discription', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'دسته بندی ',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('discription', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('price', models.BigIntegerField(default=0)),
                ('counted_view', models.IntegerField(default=0)),
                ('teacher', models.TextField()),
                ('student', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('published_date', models.DateTimeField(null=True)),
                ('category', models.ManyToManyField(to='courses.category')),
            ],
            options={
                'verbose_name': 'دوره ',
                'verbose_name_plural': 'دوره ها ',
                'ordering': ['created_date'],
            },
        ),
    ]
