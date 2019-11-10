# Generated by Django 2.2.7 on 2019-11-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191110_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagensCoisasQueGosto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_imagem', models.URLField(max_length=400, verbose_name='LinkImagem')),
                ('imagem_upload', models.ImageField(blank=True, null=True, upload_to='imagens/', verbose_name='imagemUpload')),
                ('url_sobre_a_imagem', models.URLField(max_length=400, verbose_name='linkSobreImagem')),
            ],
            options={
                'verbose_name': 'Imagem de algo que gosto',
                'verbose_name_plural': 'Imagens de coisas que gosto',
            },
        ),
        migrations.AlterField(
            model_name='imagemperfil',
            name='url',
            field=models.URLField(max_length=400, verbose_name='link'),
        ),
    ]
