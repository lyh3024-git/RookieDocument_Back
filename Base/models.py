from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(verbose_name='团队名称', max_length=20)
    add_time = models.DateTimeField(verbose_name='添加时间')

    class Meta:
        verbose_name = '团队'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class User(models.Model):
    tid = models.ForeignKey(to=Team, verbose_name='团队主键', on_delete=models.CASCADE)
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

    class Meta:
        verbose_name = '内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Fav_His(models.Model):
    cid = models.ForeignKey(to=Content, verbose_name='内容主键', on_delete=models.CASCADE)
    flag = models.CharField(verbose_name='类别', max_length=2)
    add_time = models.DateTimeField(verbose_name='添加时间')
