from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import Post
from accounts.tests.factories import CustomUserFactory


class PostFactory(factory.django.DjangoModelFactory):

    title = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(
        lambda obj: slugify(obj.title))
    author = factory.SubFactory(CustomUserFactory)
    description = factory.Faker(
        'paragraph', nb_sentences=3,
        variable_nb_sentences=True)
    content = factory.Faker(
        'paragraph', nb_sentences=10,
        variable_nb_sentences=True)

    class Meta:
        model = Post