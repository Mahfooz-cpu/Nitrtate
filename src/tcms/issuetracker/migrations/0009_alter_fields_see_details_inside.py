# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-16 11:54
from django.db import migrations, models
import tcms.issuetracker.validators


# This migration could be removed when squash migrations from scratch.


class Migration(migrations.Migration):

    dependencies = [
        ("issuetracker", "0008_add_validator_to_issue_tracker_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issuetracker",
            name="allow_add_case_to_issue",
            field=models.BooleanField(
                default=False,
                help_text="Allow to add associated test case link to issue.",
            ),
        ),
        migrations.AlterField(
            model_name="issuetracker",
            name="class_path",
            field=models.CharField(
                default="tcms.issuetracker.services.IssueTrackerService",
                help_text="Importable path to the implementation for this issue tracker. Default is <code>tcms.issuetracker.models.IssueTrackerService</code>, which provides basic functionalities for general purpose. Set to a custom path for specific class inherited from <code>IssueTrackerService</code>",
                max_length=100,
                validators=[tcms.issuetracker.validators.validate_class_path],
            ),
        ),
    ]
