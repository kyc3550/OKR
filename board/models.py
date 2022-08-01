from django.db import models

# Create your models here.

# on_delete : 회원이 없어진다면 글또한 같이 없어짐.

class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='작성인')
    write_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성 시간')
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d', default='photos.no_image.png')

    update_dttm = models.DateTimeField(auto_now=True, verbose_name = '마지막 수정일')
    hits = models.PositiveIntegerField(default=0, verbose_name = '조회수')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'