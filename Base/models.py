from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=20,unique=True)
    email = models.EmailField(verbose_name='邮箱', default='admin@admin.com')
    password = models.CharField(verbose_name='密码', max_length=20)

    class Meta:
        verbose_name = '信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Team(models.Model):
    teamname = models.CharField(verbose_name='团队名称', max_length=20, unique=True)

    class Meta:
        verbose_name = '团队'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teamname


class TeamMember(models.Model):
    tid = models.ForeignKey(to=Team, verbose_name='团队id', on_delete=models.CASCADE, related_name='team_teams')
    uid = models.ForeignKey(to=User, verbose_name='用户id', on_delete=models.CASCADE, related_name='user_teams')
    isleader = models.CharField(verbose_name='是否是创建者，1代表队长,默认0', max_length=2, default='0')
    fav = models.CharField(verbose_name='读1、写2、不可查看3，默认3', max_length=2, default='3')


class Content(models.Model):
    uid = models.ForeignKey(to=User, verbose_name='用户外键', on_delete=models.CASCADE)
    tid = models.ForeignKey(to=Team, verbose_name='团队外键-默认值为0代表该文档未加入团队', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="标题", max_length=20)
    content = models.TextField(verbose_name="内容")
    createtime = models.DateTimeField(verbose_name='创建时间')
    changetime = models.DateTimeField(verbose_name='修改时间')
    isdelete = models.CharField(max_length=2)
    isread = models.CharField(verbose_name='读1、写2、不可查看3，默认3', max_length=2, default='3')

    class Meta:
        verbose_name = '内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    detail = models.TextField(verbose_name='评论内容')
    uid = models.ForeignKey(to=User, verbose_name='用户外键', on_delete=models.CASCADE, related_name='belong_user')
    cid = models.ForeignKey(to=Content, verbose_name='文档外键', on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.detail


class Favourite(models.Model):
    cid = models.ForeignKey(to=Content, verbose_name='被收藏的文档id', on_delete=models.CASCADE)
    uid = models.ForeignKey(to=User, verbose_name='收藏者用户id', on_delete=models.CASCADE, related_name='favs')

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cid
