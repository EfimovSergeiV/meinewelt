from django.db import models



class TechModel(models.Model):
    """ Стек технологий """

    activated = models.BooleanField(verbose_name="Отображать", default=False)
    skill = models.BooleanField(verbose_name="Отображать в стеке", default=False)
    ordering = models.PositiveIntegerField(verbose_name="Сортировка", default=1)
    name = models.CharField(verbose_name="Название технологии", max_length=150)

    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "- 01. Технологии"
        ordering = ('-ordering',)

    def __str__(self):
        return self.name


class ArticleModel(models.Model):
    """ Статьи """

    tech = models.ManyToManyField(TechModel,)
    image = models.ImageField(verbose_name="Изображение", null=True, blank=True)
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    text = models.TextField(verbose_name="Текст", )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "- 02. Статьи"

    def __str__(self):
        return f"{ self.tech } / { self.title }"