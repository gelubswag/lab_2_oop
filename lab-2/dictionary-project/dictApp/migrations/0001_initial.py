# Generated by Django 5.1 on 2024-10-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255, unique=True, verbose_name='Слово')),
                ('translation', models.CharField(max_length=255, verbose_name='Перевод')),
            ],
        ),
    ]
