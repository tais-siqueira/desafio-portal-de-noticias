# Generated by Django 4.2.6 on 2023-11-24 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagem_noticia')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='imagem',
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagem_noticia',
            field=models.ImageField(blank=True, null=True, upload_to='imagem_noticia'),
        ),
        migrations.AlterField(
            model_name='categorias',
            name='categorias',
            field=models.CharField(max_length=40),
        ),
        migrations.AddField(
            model_name='imagem',
            name='noticia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.noticia'),
        ),
    ]
