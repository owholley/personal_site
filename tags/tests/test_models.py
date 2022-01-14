import pytest



from ..models import Tag
from .factories import TagFactory

pytestmark = pytest.mark.django_db

def test__str__():
    tag = TagFactory()
    assert tag.__str__() == tag.title
    assert str(tag) == tag.title