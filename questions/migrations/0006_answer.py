# Generated by Django 3.0.4 on 2020-06-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_merge_20200524_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10000)),
                ('q1', models.CharField(max_length=500)),
                ('q2', models.CharField(max_length=500)),
                ('q3', models.CharField(max_length=500)),
                ('q4', models.CharField(max_length=500)),
                ('q5', models.CharField(max_length=500)),
                ('q6', models.CharField(max_length=500)),
                ('q7', models.CharField(max_length=500)),
                ('q8', models.CharField(max_length=500)),
                ('q9', models.CharField(max_length=500)),
                ('q10', models.CharField(max_length=500)),
            ],
        ),
    ]