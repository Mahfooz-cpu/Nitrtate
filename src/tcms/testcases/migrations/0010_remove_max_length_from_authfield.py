# Generated by Django 3.0.7 on 2020-06-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testcases", "0009_remove_old_bugsystem_perms"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testcase",
            name="case_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="testcasestatus",
            name="id",
            field=models.AutoField(db_column="case_status_id", primary_key=True, serialize=False),
        ),
    ]
