# Generated by Django 4.0.6 on 2022-07-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxer', '0003_alter_boxerinfo_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxerinfo',
            name='name',
            field=models.CharField(max_length=26, verbose_name='이름'),
        ),
    ]