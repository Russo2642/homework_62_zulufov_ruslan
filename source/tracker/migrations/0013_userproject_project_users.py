# Generated by Django 4.1.7 on 2023-03-20 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0012_remove_issue_deleted_at_remove_issue_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userproject_users', to='tracker.project', verbose_name='Проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userproject_project', to=settings.AUTH_USER_MODEL, verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Проект пользователя',
                'verbose_name_plural': 'Проекты пользователя',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(related_name='projects', through='tracker.UserProject', to=settings.AUTH_USER_MODEL),
        ),
    ]