# Generated by Django 4.2.2 on 2023-07-29 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addressapp', '0007_remove_profile_profile_usercontact_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontact',
            name='profile',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myuser', to='addressapp.profile'),
        ),
    ]