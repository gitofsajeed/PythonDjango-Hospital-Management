# Generated by Django 4.0.6 on 2023-03-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('p_number', models.CharField(max_length=10)),
                ('subj', models.CharField(max_length=255)),
                ('msg', models.TextField(max_length=1000)),
            ],
        ),
    ]
