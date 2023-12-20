# Generated by Django 3.2.8 on 2023-12-20 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_alter_film_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': [django.db.models.functions.text.Lower('name')]},
        ),
        migrations.CreateModel(
            name='UserFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
