from tkinter import CASCADE
from django.db import models

# Create your models here.

class Info(models.Model):
    info_name = models.CharField(max_length=30, unique=True, verbose_name='안내사항')
    def __str__(self):
        return self.info_name
    
class TimeInfo(models.Model):   
    title = models.ForeignKey('info.Info', on_delete=models.CASCADE,verbose_name='이용시간')
    day = models.CharField(max_length=10, verbose_name='요일')
    start_time = models.TimeField(verbose_name='시작시간')
    end_time = models.TimeField(verbose_name='종료시간')
    note = models.CharField(max_length=200, verbose_name="비고", null=True, blank=True)

    class Meta:
        db_table = 'timeinfo'
        verbose_name = '이용시간'
        verbose_name_plural = '이용시간'

class PriceInfo(models.Model):
    title = models.ForeignKey('info.Info', on_delete=models.CASCADE, verbose_name='요금안내')
    registration_period = models.CharField(max_length=20, verbose_name="등록기간")
    price = models.IntegerField(verbose_name='회비')
    note = models.CharField(max_length=200, verbose_name="비고", null=True, blank=True)

    class Meta:
        db_table = 'priceinfo'
        verbose_name = '요금안내'
        verbose_name_plural = '요금안내'