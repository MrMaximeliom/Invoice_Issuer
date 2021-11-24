from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from Util.utils import rand_slug

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
        default=slugify(rand_slug()),
        verbose_name=_('Country Slug')
    )
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
        on_delete=models.CASCADE
    )
    # slug field
    slug = models.SlugField(
        default=slugify(rand_slug()),
        verbose_name=_('State Slug')
    )

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
    )
    # slug field
    slug = models.SlugField(
        default=slugify(rand_slug()),
        verbose_name=_('City Slug')
    )
