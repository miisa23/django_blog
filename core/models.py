from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.urls import reverse


# Create your models here.

# core_category


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        # ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', unique=True)
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание', blank=True, null=True)
    image = models.ImageField(verbose_name='Фото', upload_to='articles/', blank=True, null=True)
    views = models.PositiveSmallIntegerField(default=0, verbose_name='Просмотры')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'article_id': self.pk})

    def img_preview(self):
        if not self.image:
            return ''
        return mark_safe(f'<img src="{self.image.url}" width="100" height="100">')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='статья')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Отзыв')

    def __str__(self):
        return f'{self.author}: {self.article}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Like(models.Model):
    user = models.ManyToManyField(User, related_name='likes')
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='likes', blank=True, null=True)
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='likes', blank=True, null=True)


class Dislike(models.Model):
    user = models.ManyToManyField(User, related_name='dislikes')
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='dislikes', blank=True, null=True)
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='dislikes', blank=True, null=True)


