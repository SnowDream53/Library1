from django.db import models


# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)
    picture = models.URLField(blank=True, null=False)

    def get_absolute_url(self):
        return '/library/'

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/library/{self.library.id}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'