# Generated by Django 3.2.9 on 2021-11-24 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0020_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(blank=True, choices=[('R', 'Ruim'), ('P', 'Pessimo'), ('O', 'Ótimo'), ('B', 'Bom')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 14, 5, 45, 887783)),
        ),
    ]
