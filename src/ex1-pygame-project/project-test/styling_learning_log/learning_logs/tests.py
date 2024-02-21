from django.test import TestCase
from learning_logs.models import Topic

# Create your tests here.

class TopicTestCase(TestCase):
    def setUp(self):
        Topic.objects.create(text="test topic")

    def test_topic_name(self):
        """Topic name is correct"""
        topic = Topic.objects.get(text="test topic")
        self.assertEqual(topic.name, 'test topic')
