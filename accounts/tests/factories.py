from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import CustomUser

class CustomUserFactory(factory.django.DjangoModelFactory):

    username = factory.fuzzy.FuzzyText()

    class Meta:
        model = CustomUser