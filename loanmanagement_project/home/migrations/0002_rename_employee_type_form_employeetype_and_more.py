# Generated by Django 4.2.7 on 2023-11-15 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='employee_type',
            new_name='employeeType',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='amount',
            new_name='loanAmount',
        ),
    ]