# Generated by Django 4.2.6 on 2023-12-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_categorias_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='categoria',
            field=models.CharField(default='Música, Entrevista, Filme', max_length=100),
        ),
    ]
