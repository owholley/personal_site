from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel

class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField("Post Address", always_update=False, populate_from="title")
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    # content = RichTextField(blank=False)
    content = models.TextField(blank=False)

    class Meta:
        ordering = ['-modified']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={"slug": self.slug})
