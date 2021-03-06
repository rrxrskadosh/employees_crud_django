# Generated by Django 2.2.19 on 2021-04-13 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_role', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=150)),
                ('active', models.BooleanField(verbose_name=True)),
                ('department', models.CharField(max_length=150)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
