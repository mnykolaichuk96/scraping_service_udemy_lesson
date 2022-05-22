from django.db import models

from scraping.utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name="Населений пункт",
                            unique=True)
    slug = models.SlugField(blank=True,
                            unique=True)

    class Meta:
        verbose_name='Населений пункт'
        verbose_name_plural = 'Населені пункти'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name="Мова програмування",
                            unique=True)
    slug = models.SlugField(blank=True,
                            unique=True)

    class Meta:
        verbose_name = 'Мова програмування'
        verbose_name_plural = 'Мови програмування'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250,
                             verbose_name='Заголовок')
    company = models.CharField(max_length=250,
                             verbose_name='Компанія')
    description = models.TextField(verbose_name='Опис')

    city = models.ForeignKey(City,
                             on_delete=models.PROTECT,
                             verbose_name='Населений пункт')
    language = models.ForeignKey(Language,
                                 on_delete=models.PROTECT,
                                 verbose_name='Мова програмування')

    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'

    def __str__(self):
        return self.title