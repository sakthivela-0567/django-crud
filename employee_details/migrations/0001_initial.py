# Generated by Django 4.0.3 on 2022-03-15 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=100)),
                ('business_reg_no', models.CharField(max_length=5)),
                ('Email', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('region_based_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_details.region')),
            ],
        ),
    ]