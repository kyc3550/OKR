from django.db import models

# Create your models here.

class BoxerInfo(models.Model):
    name =  models.CharField(max_length=50, verbose_name='이름')
    age = models.DateTimeField(null=True, blank=True,max_length=8 ,verbose_name='나이')
    weight = models.CharField(max_length=30, verbose_name='체급')
    total = models.IntegerField(verbose_name='전')
    win = models.IntegerField(verbose_name='승')
    lose = models.IntegerField(verbose_name='패')
    draw = models.IntegerField(verbose_name='무승부')
    image = models.ImageField(verbose_name='사진',upload_to = 'photos/%Y/%m/%d', default='photos.no_image.png')
    note = models.CharField(max_length=200, verbose_name="수상", null=True, blank=True)

    class Meta:
        db_table = 'boxer_info'
        verbose_name = '선수소개'
        verbose_name_plural = '선수소개'
        