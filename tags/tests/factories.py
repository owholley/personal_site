from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import Tag
from blog.tests.factories import PostFactory


class TagFactory(factory.django.DjangoModelFactory):

    title = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(
        lambda obj: slugify(obj.title))
    description = factory.Faker(
        'paragraph', nb_sentences=3,
        variable_nb_sentences=True)
    tags = factory.RelatedFactory(
        PostFactory,)
    
    class Meta:
        model = Tag