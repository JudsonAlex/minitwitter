# Generated by Django 4.2.1 on 2023-05-25 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('conteudo', models.CharField(max_length=1000)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
