# Generated by Django 2.1.7 on 2019-03-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='estado',
            field=models.CharField(choices=[('AC', 'Acre'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo')], default='AC', max_length=2),
        ),
    ]
