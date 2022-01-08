from django.db import models

from autoslug import AutoSlugField

from blog.models import Post


class Tag(models.Model):
    title = models.CharField(max_length=25)
    slug = AutoSlugField("Tag Address", always_update=False, populate_from="title")
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Post)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

