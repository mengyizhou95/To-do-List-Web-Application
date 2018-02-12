# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TodoList(models.Model):
    content = models.CharField(max_length=255, blank=False, null=False)
    is_completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Item: Content {} : IsCompleted {}'.format(
            self.content,
            self.is_completed,
        )

    class Meta:
        ordering = ('is_completed', '-update_at')
