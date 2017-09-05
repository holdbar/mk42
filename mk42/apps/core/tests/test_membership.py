# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/tests/test_membership.py

from __future__ import unicode_literals

from django.test import TestCase

from mk42.apps.users.models.user import User
from mk42.apps.core.models.group import Group
from mk42.apps.core.models.membership import Membership



__all__ = [
    "MembershipTestCase",
]


class MembershipTestCase(TestCase):
    """
    Membership test case.
    """

    def setUp(self):
        self.user, self.user_created = User.objects.get_or_create(username="tester", password="qwerty123")
        self.group, self.group_created = Group.objects.get_or_create(name="Autotest group", description="Just a test group", owner=self.user)
        
    def test_membership_creation(self):  
        self.assertQuerysetEqual(self.user.membership.filter(group=self.group), map(repr, Membership.objects.filter(user=self.user, group=self.group)))

    def test_active_queryset(self):
        self.assertQuerysetEqual(Membership.objects.filter(active=True), map(repr, Membership.objects.active()))

    def test_inactive_queryset(self):
        self.assertQuerysetEqual(Membership.objects.filter(active=False), map(repr, Membership.objects.inactive()))
        
