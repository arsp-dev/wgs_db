# Generated by Django 4.2.7 on 2023-11-09 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wgs_app", "0007_qualifyr_accession_no_alter_qualifyr_sample_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="qualifyr", name="accession_no",),
    ]