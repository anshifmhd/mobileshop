# Generated by Django 4.0.5 on 2022-12-16 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
