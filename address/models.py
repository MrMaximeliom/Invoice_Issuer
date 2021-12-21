from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

# country class  is responsible for modeling country attributes and functions
class Country(models.Model):
    # country name field
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    # country name abbreviation field
    name_abbreviation = models.CharField(
        max_length=10,
        blank=True
    )
    # country name slug field
    slug = models.SlugField(
        verbose_name=_('Country Slug')
    )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    # specifying "name" field as reference name in relations
    def __str__(self):
        return self.name
# State class is responsible for modeling states attributes and functions
class State(models.Model):
    # name field
    name = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )
    # foreign key refers to Country table
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='states'
    )
    # slug field
    slug = models.SlugField(
        verbose_name=_('State Slug')
    )

    # specifying "name" field as reference name in relations
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class City(models.Model):
    # name field
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )
    # foreign key refers to State model
    State = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='cities'
    )
    # slug field
    slug = models.SlugField(
        verbose_name=_('City Slug')
    )
    # specifying "name" field as reference name in relations
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
