# Generated by Django 4.2.15 on 2024-09-09 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GeekTide_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='published_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=141441, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
