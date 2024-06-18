from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Teg(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    articl = models.ManyToManyField(Article, verbose_name='ArticletAG')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class ArticleTeg(models.Model):
    article = models.ForeignKey(Article, related_name='scopes', on_delete=models.CASCADE)
    teg = models.ForeignKey(Teg, verbose_name='Категория', on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной')