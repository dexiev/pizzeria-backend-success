# Generated by Django 3.2.1 on 2021-12-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(db_index=True, default=0, max_length=200, verbose_name='Description'),
        ),
    ]