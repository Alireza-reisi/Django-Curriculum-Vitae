# Generated by Django 5.0.3 on 2024-04-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('timeline', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
        ),
    ]
