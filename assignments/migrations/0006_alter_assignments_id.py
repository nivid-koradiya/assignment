# Generated by Django 4.0.5 on 2022-06-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_alter_assignments_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False),
        ),
    ]