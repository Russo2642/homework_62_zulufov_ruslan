# Generated by Django 4.1.7 on 2023-03-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_remove_issue_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='types',
            field=models.ManyToManyField(related_name='issue', to='tracker.type'),
        ),
    ]