# Generated by Django 3.2.9 on 2021-11-23 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0018_auto_20211028_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 13, 23, 50, 31411)),
        ),
    ]
