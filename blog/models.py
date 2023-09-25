from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='заголовок')
    text_body = models.TextField(verbose_name='содержание статьт')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    count_of_views = models.IntegerField(default=0, verbose_name="количество просмотров", **NULLABLE)
    publication_date = models.DateTimeField(auto_created=True, verbose_name="дата публикации", **NULLABLE)

    def __str__(self):
        return f'{self.title, self.count_of_views}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
