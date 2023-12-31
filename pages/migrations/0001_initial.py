# Generated by Django 4.2.4 on 2023-08-26 05:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('displayed_name', models.CharField(max_length=120)),
                ('message', models.TextField(max_length=1000)),
                ('reviewed', models.BooleanField(default=False)),
                ('publish', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
