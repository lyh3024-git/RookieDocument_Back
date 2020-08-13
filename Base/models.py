from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=20)
    email = models.EmailField(verbose_name='邮箱', default='admin@admin.com')
    password = models.CharField(verbose_name='密码', max_length=20)

    class Meta:
        verbose_name = '信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Content(models.Model):
    title = models.CharField(verbose_name="标题", max_length=20)
    content = models.TextField(verbose_name="内容")