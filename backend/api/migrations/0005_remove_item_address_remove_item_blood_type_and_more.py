# Generated by Django 5.0.4 on 2024-07-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_item_father_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='address',
        ),
        migrations.RemoveField(
            model_name='item',
            name='blood_type',
        ),
        migrations.RemoveField(
            model_name='item',
            name='citizenship',
        ),
        migrations.RemoveField(
            model_name='item',
            name='civil_status',
        ),
        migrations.RemoveField(
            model_name='item',
            name='college',
        ),
        migrations.RemoveField(
            model_name='item',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='item',
            name='elementary',
        ),
        migrations.RemoveField(
            model_name='item',
            name='email',
        ),
        migrations.RemoveField(
            model_name='item',
            name='father_first_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='father_last_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='father_middle_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='height',
        ),
        migrations.RemoveField(
            model_name='item',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='mother_first_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='mother_last_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='mother_middle_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='item',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='item',
            name='place_of_birth',
        ),
        migrations.RemoveField(
            model_name='item',
            name='secondary',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='item',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='item',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='item',
            name='middlena_me',
            field=models.CharField(default='Babaero', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='first_name',
            field=models.CharField(default='John', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='last_name',
            field=models.CharField(default='Dela Cruz', max_length=100),
        ),
    ]
