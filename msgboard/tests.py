# from django.test import TestCase

# Create your tests here.
import pytest
from django.db.models.query import QuerySet
from .models import Message

def test_with_client(client):
    response = client.get('/posts')
    assert response.status_code == 301
    response = client.get(response.url)
    assert b"article1" in response.content


@pytest.mark.django_db
class TestMessage:
    def test_main_feed(cls):
        out = Message.main_feed()
        assert isinstance(out, QuerySet)
        assert all(isinstance(m, Message) for m in out)
        assert list(out.values_list('author', 'text')) == [
            ('Test User2', 'Another simple test message'),
            ('Test User1', 'A simple test message'),
        ]
