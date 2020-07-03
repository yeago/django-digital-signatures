# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=55)),
                ('date_created', models.DateTimeField(editable=False)),
                ('object_pk', models.IntegerField(null=True, editable=False, blank=True)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.deletion.CASCADE)),
                ('content_type', models.ForeignKey(blank=True, editable=False, to='contenttypes.ContentType', null=True, on_delete=models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Signatory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('auth_token', models.CharField(max_length=255)),
                ('date_signed', models.DateTimeField(editable=False)),
                ('document', models.ForeignKey(to='django_digital_signature.Document', on_delete=models.deletion.CASCADE)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.deletion.CASCADE)),
            ],
        ),
    ]
