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

class Tag(models.Model):
    article = models.ManyToManyField(Article, related_name='tags',through='Scope')
    name = models.CharField(max_length=50, verbose_name='Название', )
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тег'
        
    def __str__(self):
        return self.name
    
class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Название статьи')
    is_main = models.BooleanField(verbose_name='Основной')
    
    class Meta:
        verbose_name = 'Принадлежность'
        verbose_name_plural = 'Принадлежность'