# Generated by Django 3.2.9 on 2021-11-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_tourmodel_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tourtagmodel',
            options={'verbose_name': 'tour tag', 'verbose_name_plural': 'tour tags'},
        ),
        migrations.AlterField(
            model_name='tourmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='tourmodel',
            name='discount',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='tourmodel',
            name='price',
            field=models.IntegerField(default=0, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='tourmodel',
            name='title',
            field=models.CharField(max_length=30, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='tourtagmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_at'),
        ),
        migrations.AlterField(
            model_name='tourtagmodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]
