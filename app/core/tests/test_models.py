from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful"""
        email = "test@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)

    def test_new_user_email_normalized(self):
        """test the email for a new user is normilized"""
        email = 'test@GMAILGMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_invalid(self):
        """test if the email is invalid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'asdqw12')

    def test_create_new_super_user(self):
        """Test create new super user"""
        user = get_user_model().objects.create_superuser(
            'test@asdqwd.dk',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
