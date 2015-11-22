# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
<<<<<<< HEAD
from django.conf import settings
=======
>>>>>>> 8da517b39a1f3428cbb0342a2083e8ec1e0cda8b


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> 8da517b39a1f3428cbb0342a2083e8ec1e0cda8b
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('website', models.URLField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
=======
            name='events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=40)),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
>>>>>>> 8da517b39a1f3428cbb0342a2083e8ec1e0cda8b
        ),
    ]
