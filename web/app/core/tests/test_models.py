"""
Tests for Core Models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models."""

    def test_create_user_with_email_successful(self):
        """TEST: Creating a user with an email is successful."""
        email = 'test@test.com'
        password = 'Test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """TEST: Email normalized for new users."""
        sample_emails = [
            ['test1@TEST.com', 'test1@test.com'],
            ['Test2@Test.com', 'Test2@test.com'],
            ['TEST3@TEST.COM', 'TEST3@test.com'],
            ['test4@test.COM', 'test4@test.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'Test@123')
            self.assertEqual(user.email, expected)

    def test_new_user_invalid_email(self):
        """TEST: Creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Test@123')

    def test_create_new_superuser(self):
        """TEST: Creating new superuser """
        user = get_user_model().objects.create_superuser(
            'admin@test.com',
            'Test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
