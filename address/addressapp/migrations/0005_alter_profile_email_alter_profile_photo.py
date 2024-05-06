# Generated by Django 4.2.2 on 2023-07-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressapp', '0004_remove_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='manasa.jpeg', upload_to='images/'),
        ),
    ]
