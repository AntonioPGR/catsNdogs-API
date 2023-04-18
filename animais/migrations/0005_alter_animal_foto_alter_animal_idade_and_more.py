# Generated by Django 4.2 on 2023-04-17 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0004_rename_especies_especie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='foto',
            field=models.ImageField(blank=True, default='/media/Animais/2023/04/13/doguinho.jpg', upload_to='Animais/%Y/%m/%d', verbose_name='Foto do animal'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='idade',
            field=models.PositiveIntegerField(verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='telefone_contato',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='Telefone para contato'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='nome',
            field=models.CharField(max_length=30, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='raca',
            name='nome',
            field=models.CharField(max_length=30, unique=True, verbose_name='Nome'),
        ),
    ]
