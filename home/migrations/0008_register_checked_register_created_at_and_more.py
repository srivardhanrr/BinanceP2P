# Generated by Django 4.1.6 on 2023-02-22 06:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='checked',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='No', max_length=5),
        ),
        migrations.AddField(
            model_name='register',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]