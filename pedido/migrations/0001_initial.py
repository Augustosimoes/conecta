# Generated by Django 2.1 on 2018-08-29 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0007_auto_20180828_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.Cliente')),
            ],
        ),
    ]
