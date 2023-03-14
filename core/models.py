from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    create = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Modified", auto_now=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        abstract: bool = True


class Services(Base):
    icons = (
        ("lni-cog", "Engrenagem"),
        ("lni-stats-up", "Grafico"),
        ("lni-users", "Usuários"),
        ("lni-layers", "Design"),
        ("lni-mobile", "Mobile"),
        ("lni-rocket", "Foguete"),
    )
    service = models.CharField("Service", max_length=100)
    description = models.TextField("Description", max_length=100)
    icon = models.CharField("Icon", max_length=12, choices=icons)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = "Services"

    def __repr__(self) -> str:
        return str(self.service)


class Profission(Base):
    profission = models.CharField("Profission", max_length=100)

    class Meta:
        verbose_name = 'Profission'
        verbose_name_plural = 'Profissionals'


class Team(Base):
    name = models.CharField("Name", max_length=100)
    profission = models.ForeignKey('core.Profission', verbose_name='Profission',
                                   on_delete=models.CASCADE)
    description = models.TextField("Description", max_length=200)
    image = StdImageField("Image", upload_to='team', variations={'thumb': {'width': 480,
                                                                      'heigth': 480,
                                                                           'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Teams'

    def __repr__(self) -> str:
        return str(self.name)
