# -*- coding: utf-8 -*-
from django.db import models
# from django.contrib.auth.forms import User
from django.contrib.auth.models import AbstractUser
import re
from django.core.validators import ValidationError


def validate_user(username):
    reg_en_obj = re.compile(r'^[a-zA-Z0-9_]$')
    reg_cn_obj = re.compile(r'^[\u4e00-\u9fa5]$')
    # 中英混合只能遍历验证
    print('--------username-------------'.format(username))
    if len(username) <= 0:
        raise ValidationError('昵称不能为空-_-')
    for a in username:
        if not reg_en_obj.search(a) and not reg_cn_obj.search(a):
            raise ValidationError('用户昵称由汉字,字母,数字,或者下划线组成-_-')

def validate_password(password):
    reg_en_obj = re.compile(r'^[a-zA-Z0-9_@.]$')
    # 中英混合只能遍历验证
    print('--------password-------------'.format(password))
    if len(username) <= 6:
        raise ValidationError('密码长度不能小于6-_-')
    for a in username:
        if not reg_en_obj.search(a):
            raise ValidationError('用户密码由字母,数字,或者下划线@.组成-_-')

class User(models.Model):
    nickname = models.CharField(max_length=32, validators=[validate_user], unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    email_verify_code = models.CharField(max_length=6)

    def __str__(self):
        return self.nickname

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
