# Generated by Django 4.2.2 on 2023-07-01 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_alter_item_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='create_by',
            new_name='created_by',
        ),
    ]