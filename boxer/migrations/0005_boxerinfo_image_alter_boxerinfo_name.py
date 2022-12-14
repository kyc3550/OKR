# Generated by Django 4.0.6 on 2022-07-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxer', '0004_alter_boxerinfo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxerinfo',
            name='image',
            field=models.ImageField(default='photos.no_image.png', upload_to='photos/%Y/%m/%d', verbose_name='사진'),
        ),
        migrations.AlterField(
            model_name='boxerinfo',
            name='name',
            field=models.CharField(max_length=50, verbose_name='이름'),
        ),
    ]
