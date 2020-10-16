# Generated by Django 2.1.5 on 2020-10-16 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentperformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.TextField()),
                ('sex', models.TextField()),
                ('age', models.BigIntegerField()),
                ('address', models.TextField()),
                ('famsize', models.TextField()),
                ('Pstatus', models.TextField()),
                ('Medu', models.BigIntegerField()),
                ('Fedu', models.BigIntegerField()),
                ('Mjob', models.TextField()),
                ('Fjob', models.TextField()),
                ('reason', models.TextField()),
                ('father', models.TextField()),
                ('traveltime', models.BigIntegerField()),
                ('studytime', models.BigIntegerField()),
                ('failures', models.BigIntegerField()),
                ('schoolsup', models.TextField()),
                ('famsup', models.TextField()),
                ('paid', models.TextField()),
                ('activities', models.TextField()),
                ('nursery', models.TextField()),
                ('higher', models.TextField()),
                ('internet', models.TextField()),
                ('romantic', models.TextField()),
                ('famrel', models.BigIntegerField()),
                ('freetime', models.BigIntegerField()),
                ('goout', models.BigIntegerField()),
                ('Dalc', models.BigIntegerField()),
                ('Walc', models.BigIntegerField()),
                ('health', models.BigIntegerField()),
                ('absences', models.BigIntegerField()),
                ('G1', models.BigIntegerField()),
                ('G2', models.BigIntegerField()),
                ('G3', models.BigIntegerField()),
            ],
        ),
    ]
