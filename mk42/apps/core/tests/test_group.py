# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/tests/test_group.py

from __future__ import unicode_literals

from django.test import TestCase

from mk42.apps.users.models.user import User
from mk42.apps.core.models.group import Group



__all__ = [
    "GroupTestCase",
]


class GroupTestCase(TestCase):
    """
    Group test case.
    """

    def setUp(self):
        self.user, self.user_created = User.objects.get_or_create(username="tester", password="qwerty123")
        self.group, self.group_created = Group.objects.get_or_create(name="Autotest group", description="Just a test group", owner=self.user)
        
    def test_group_creation(self):  
        self.assertEqual(self.group_created, True)

    def test_active_queryset(self):
        self.assertQuerysetEqual(Group.objects.filter(active=True), map(repr, Group.objects.active()))

    def test_inactive_queryset(self):
        self.assertQuerysetEqual(Group.objects.filter(active=False), map(repr, Group.objects.inactive()))
        
