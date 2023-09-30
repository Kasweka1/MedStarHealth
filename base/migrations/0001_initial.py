# Generated by Django 4.2.5 on 2023-09-24 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('initials', models.CharField(blank=True, max_length=20, null=True)),
                ('sex', models.CharField(max_length=1)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('post_code', models.CharField(blank=True, max_length=6, null=True)),
                ('admission', models.DateField(blank=True, null=True)),
                ('dob', models.DateField(db_column='DOB')),
                ('pat_next_kin', models.CharField(blank=True, db_column='PAT_NEXT_KIN', max_length=20, null=True)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('ward_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('ward_name', models.CharField(blank=True, max_length=25, null=True)),
                ('number_beds', models.IntegerField(blank=True, null=True)),
                ('nurse_in_charge', models.CharField(max_length=20)),
                ('ward_type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'ward',
                'managed': False,
            },
        ),
    ]