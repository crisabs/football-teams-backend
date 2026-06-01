# Generated migration to remove blank=True and null=True from achievement fields

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("achievement", "0004_alter_achievement_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playerachievement",
            name="achievement",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="player_achievements",
                to="achievement.achievement",
            ),
        ),
        migrations.AlterField(
            model_name="teamachievement",
            name="achievement",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="team_achievements",
                to="achievement.achievement",
            ),
        ),
    ]
