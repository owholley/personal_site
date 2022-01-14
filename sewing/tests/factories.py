from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import Product, Image


class ProductFactory(factory.django.DjangoModelFactory):

    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(
        lambda obj: slugify(obj.name))
    description = factory.Faker(
        'paragraph', nb_sentences=3,
        variable_nb_sentences=True)

    class Meta:
        model = Product


class ImageFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    product = factory.SubFactory(ProductFactory)
    slug = factory.LazyAttribute(
        lambda obj: slugify(obj.name))
    

    class Meta:
        model = Image