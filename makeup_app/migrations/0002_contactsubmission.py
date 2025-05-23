# Generated by Django 5.2 on 2025-05-01 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('product', models.CharField(blank=True, max_length=200, null=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
