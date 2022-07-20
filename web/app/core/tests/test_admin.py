from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Tests for Django Admin."""

    def setUp(self):
        """
        Mandatory setup for tests - create User and Client.
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='superadmin@test.com',
            password='Test@123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='regularuser@test.com',
            password='Test@123',
            name='Regular User'
        )

    # def test_users_list(self):
    #     """TEST: Users are listed on user page."""
    #     url = reverse('admin:core_user_changelist')
    #     res = self.client.get(url)

    #     self.assertContains(res, self.user.name)
    #     self.assertContains(res, self.user.email)

    # def test_user_change_page(self):
    #     """TEST: User edit page works."""
    #     url = reverse('admin:core_user_change', args=[self.user.id])
    #     res = self.client.get(url)

    #     self.assertEqual(res.status_code, 200)

    # def test_create_user_page(self):
    #     """TEST: Create users page work."""
    #     url = reverse('admin:core_user_add')
    #     res = self.client.get(url)

    #     self.assertEqual(res.status_code, 200)
