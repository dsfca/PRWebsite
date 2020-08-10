# Generated by Django 2.1.7 on 2019-04-29 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExercicioFicheiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_ficheiro', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ExercicioSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_exercicio', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='exercicioficheiro',
            name='exercicio_Slide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo.ExercicioSlide'),
        ),
    ]