# Generated by Django 4.1.6 on 2023-02-10 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_remove_learner_social_link_user_social_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_instructor',
            field=models.BooleanField(default=False),
        ),
    ]
