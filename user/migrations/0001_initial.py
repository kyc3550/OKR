# Generated by Django 4.0.6 on 2022-07-15 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32, unique=True, verbose_name='아이디')),
                ('user_pw', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('user_name', models.CharField(max_length=26, unique=True, verbose_name='이름')),
                ('user_phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(regex='^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')], verbose_name='핸드폰 번호')),
                ('user_register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='계정 생성 시간')),
                ('user_gender', models.SmallIntegerField(choices=[(0, '여자'), (1, '남자'), (2, '잘못된 입력')])),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
                'db_table': 'user',
                'ordering': ['-user_name'],
            },
        ),
    ]
