# Generated by Django 4.2.4 on 2023-11-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_ord_delete_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ord',
            old_name='items',
            new_name='Items',
        ),
        migrations.AddField(
            model_name='ord',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]