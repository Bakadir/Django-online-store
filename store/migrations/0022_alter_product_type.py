# Generated by Django 4.1.3 on 2023-10-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_club_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('home', 'home'), ('away', 'away'), ('third', 'third'), ('Special Edition', 'Special Edition'), ('Special Edition 2', 'Special Edition 2'), ('Special Edition 3', 'Special Edition 3'), ('Special Edition 4', 'Special Edition 4')], max_length=100),
        ),
    ]