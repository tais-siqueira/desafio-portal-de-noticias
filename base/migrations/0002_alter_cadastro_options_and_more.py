# Generated by Django 4.2.6 on 2023-11-13 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastro',
            options={'ordering': ['-data'], 'verbose_name': 'Usuário Cadastrado', 'verbose_name_plural': 'Usuários Cadastrados'},
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='nome',
            new_name='categoria',
        ),
    ]
