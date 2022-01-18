# Generated by Django 3.2 on 2022-01-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RosterList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name Of List')),
                ('points', models.CharField(max_length=4, verbose_name='Points')),
                ('faction', models.CharField(max_length=50, verbose_name='Faction')),
                ('roster', models.TextField(verbose_name='Roster')),
                ('createdBy', models.CharField(max_length=50, verbose_name='Created By')),
                ('createdOn', models.DateField(verbose_name='Created On')),
                ('numberOfComments', models.CharField(max_length=50, verbose_name='Number Of Comments')),
                ('numberOfLikes', models.CharField(max_length=50, verbose_name='Number Of Likes')),
                ('numberOfDislikes', models.CharField(max_length=50, verbose_name='Number Of Dislikes')),
            ],
        ),
    ]