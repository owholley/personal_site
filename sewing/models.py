from django.db import models
from django.utils.html import mark_safe
from django.urls import reverse

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

class Product(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = AutoSlugField("Product Address", always_update=False, populate_from='name')
    description = models.TextField(blank=False)

    class Meta:
        ordering = ['-modified']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sewing:detail', kwargs={"slug": self.slug})


class Image(TimeStampedModel):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images")
    slug = AutoSlugField(
        "Image Address",
        always_update=False,
        populate_from='name')
    url = models.ImageField(upload_to='sewing/')

    def __str__(self):
        return self.name

    @property
    def thumbnail_preview(self):
        if self.url:
            return mark_safe('<img src="{}"  width="auto" height="200" />'.format(self.url.url))
        return ""

