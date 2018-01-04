# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile', on_delete=models.CASCADE)
    profile_image = models.FileField(upload_to='profile_image')

    def __str__(self):
        return self.belong_to.username



class Article(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    # owner = models.ForeignKey(to=UserProfile, related_name='videos', default=1)
    AUTHOR_CHOICES = (
        ('hedongjun', '河东君'),
        ('lorelei', 'Lorelei'),
        ('jikegongdongdui', '鸡壳攻动队'),
    )
    author = models.CharField(choices=AUTHOR_CHOICES, max_length=32)
    # author = models.ForeignKey(to=UserProfile, related_name='articles', default=1, on_delete=models.CASCADE)
    introduction = models.CharField(null=True, blank=True, max_length=255)
    content = models.TextField(null=True, blank=True)
    cover = models.FileField(upload_to='cover_image', null=True)
    # articles category
    MAIN_CATE_CHOICES = (
        ('fuxi', '祓禊'),
        ('yunji', '云笈'),
        ('saibo', '赛博'),
    )
    main_category = models.CharField(choices=MAIN_CATE_CHOICES, max_length=32)
    SUB_CATE_CHOICES = (
        ('wuxian', '武侠'),
        ('xianxia', '仙侠'),
        ('xuanhuan', '玄幻'),
        ('yunjiqiqian', '云笈七签'),
        ('xuanhuan', '浴乎沂'),
        ('fenghuwuyu', '风乎舞雩'),
        ('yongergui', '咏而归'),
        ('chunqiuerxi', '春秋二禊'),
        ('kehuan', '科幻'),
        ('qihuan', '奇幻'),
        ('mohuan', '魔幻'),
        ('lapusaibo', '拉普赛博'),
    )
    sub_category = models.CharField(choices=SUB_CATE_CHOICES, max_length=32)

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

# 文章主分类
# class Article_Main_Category(models.Model):
#     CATE_CHOICES = (
#         ('fuxi', '祓禊'),
#         ('yunji', '云笈'),
#         ('saibo', '赛博'),
#     )
#     art_main_category = models.CharField(choices=CATE_CHOICES, max_length=16)
#     # video = models.ForeignKey(to=Video, related_name='tickets', on_delete=models.CASCADE)
#     main_article = models.ForeignKey(to=Article, related_name='article_main_category', on_delete=models.CASCADE)
#     def __str__():
#         return self.art_main_category

# 文章二级分类
# class Article_Sub_Category(models.Model):
#     CATE_CHOICES = (
#         ('wuxian', '武侠'),
#         ('xianxia', '仙侠'),
#         ('xuanhuan', '玄幻'),
#         ('yunjiqiqian', '云笈七签'),
#         ('xuanhuan', '浴乎沂'),
#         ('fenghuwuyu', '风乎舞雩'),
#         ('yongergui', '咏而归'),
#         ('chunqiuerxi', '春秋二禊'),
#         ('kehuan', '科幻'),
#         ('qihuan', '奇幻'),
#         ('mohuan', '魔幻'),
#         ('lapusaibo', '拉普赛博'),
#     )
#     art_sub_category = models.CharField(choices=CATE_CHOICES, max_length=16)
#     sub_article = models.ForeignKey(to=Article, related_name='article_sub_category', on_delete=models.CASCADE)
#
#     def __str__():
#         return self.art_sub_category
