# Generated by Django 4.0.4 on 2022-05-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='write your name', max_length=50)),
                ('reviews_description', models.TextField(help_text='write your review')),
                ('reviews_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
