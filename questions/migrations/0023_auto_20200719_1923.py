# Generated by Django 3.0.1 on 2020-07-19 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_member_address'),
        ('questions', '0022_merge_20200719_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='userID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Member'),
        ),
    ]
