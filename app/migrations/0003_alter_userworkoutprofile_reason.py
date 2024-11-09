# Generated by Django 5.1.3 on 2024-11-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_userworkoutprofile_remove_workoutsession_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userworkoutprofile",
            name="reason",
            field=models.CharField(
                choices=[
                    ("WL", "Weight Loss"),
                    ("MG", "Muscle Gain"),
                    ("FL", "Flexibility"),
                    ("EN", "Endurance"),
                    ("GH", "General Health"),
                ],
                help_text="Workout goal",
                max_length=2,
            ),
        ),
    ]