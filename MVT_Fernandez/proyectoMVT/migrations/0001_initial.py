# Generated by Django 4.1.2 on 2022-11-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('camiseta', models.IntegerField()),
                ('nacimiento', models.DateField()),
            ],
        ),
    ]
