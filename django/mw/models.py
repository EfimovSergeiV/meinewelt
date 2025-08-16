from django.db import models


class ProjectModel(models.Model):

    STATUS_VARS = [
        ( "prod", "В сети" ),
        ( "dev", "В разработке" ),
        ( "other", "Прочие" ),
    ]

    status = models.CharField(verbose_name="Статус", max_length=255, choices=STATUS_VARS, default="dev")
    url = models.URLField(verbose_name="Ссылка", null=True, blank=True)
    name = models.CharField(verbose_name="Название", max_length=255, null=True, blank=True)
    created = models.DateField(verbose_name="Дата создания", null=True, blank=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = [ "created", ]

    def __str__(self):
        return self.name