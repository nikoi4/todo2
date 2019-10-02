from django.contrib.auth.models import User
from django.test import (
    TestCase,
    Client,
)
from django.urls import reverse_lazy

from tasks.models import (
    Tasks,
    Priorities,
)
# Create your tests here.

TASK = {
    'name': 'ver el partido',
    'event_id': '1414',
}


class TestTasksCreate(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='nico',
            password='123456',
        )
        self.priority = Priorities.objects.create(name='High')
        self.client = Client()
        self.client.force_login(self.user)

    def test_task_creation(self):
        task = Tasks(**TASK)
        task.priority = self.priority
        task.user = self.user

        task.save()

        self.assertEqual(task.name, 'ver el partido')

    def test_task_post(self):
        self.client.post(
            reverse_lazy('tasks-new'), {
                'name': 'ver el partido',
                'event_id': '1414',
                'priority': '1',
                'user': '1'
            },
            # follow=True
        )
        self.assertEqual(Tasks.objects.count(), 1)
