from django.db import models
from django.conf import settings


# Create your models here.
class Priorities(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    event_id = models.CharField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )
    priority = models.ForeignKey(Priorities, on_delete=models.CASCADE)

    def __str__(self):
        return (
            '\n name: {}'
            '\n priority: {}'
            '\n done? {}'
            '\n updated: {}'
            '\n event_id: {}'
            '\n user: {}'
        ).format(
            self.name,
            self.priority,
            self.done,
            self.updated_on,
            self.event_id,
            self.user
        )
