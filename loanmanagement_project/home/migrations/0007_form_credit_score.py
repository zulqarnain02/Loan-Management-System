# Generated by Django 4.2.7 on 2023-11-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_form_employeetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='credit_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]