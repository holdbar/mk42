# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/tests/test_event.py

from __future__ import unicode_literals

from django.test import TestCase

from mk42.apps.users.models.user import User
from mk42.apps.core.models.group import Group
from mk42.apps.core.models.event import Event



__all__ = [
    "EventTestCase",
]


class EventTestCase(TestCase):
    """
    Event test case.
    """

    def setUp(self):
        self.user, self.user_created = User.objects.get_or_create(username="tester", password="qwerty123")
        self.group, self.group_created = Group.objects.get_or_create(name="Autotest group", description="Just a test group", owner=self.user)
        # TODO: solve issue with validation of wrong dates or remove dates test
        self.event, self.event_created = Event.objects.get_or_create(name="Autotest event", group=self.group)

    def test_event_creation(self):  
        self.assertEqual(self.event_created, True)

    def test_status(self):  
        self.assertEqual(self.event.status, 1)

    def test_human_readable_status(self):   
        self.assertEqual(self.event.human_readable_status, "Pending")
