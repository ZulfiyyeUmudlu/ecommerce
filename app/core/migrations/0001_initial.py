# Generated by Django 5.0.3 on 2024-04-20 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo_home',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contact.contactinfo')),
                ('textt', models.TextField()),
            ],
            bases=('contact.contactinfo',),
        ),
    ]
