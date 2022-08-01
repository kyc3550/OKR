from django.db import models
from django.core.validators import RegexValidator

GENDER_CHOICES = (
    (0, '여자'),
    (1, '남자'),
)
# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='아이디')
    user_pw = models.CharField(max_length=128, verbose_name='비밀번호')
    user_name = models.CharField(max_length=26, unique=True, verbose_name='이름')
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    user_phone_number = models.CharField(validators=[phoneNumberRegex], max_length=11, unique=True, verbose_name='핸드폰 번호')
    user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='계정 생성 시간')
    user_gender = models.SmallIntegerField(choices=GENDER_CHOICES)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['-user_name']
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'