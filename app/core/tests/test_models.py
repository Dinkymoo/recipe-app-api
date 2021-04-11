from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import models


def create_test_user(email='testuser@test.com', password="testpassword"):
    return get_user_model().create_user(email=email, password=password)


class ModelTest(TestCase):

    def test_create_user_with_email_successfully(self):
        """Test creating user is successful"""
        email = 'test@test.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@THRTHvmvmv.COM"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises errors"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_user_superuser(self):
        """Test creating a new superuser"""
        email = "test@THRTHvmvmv.COM"
        user = get_user_model().objects.create_superuser(email, 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=create_test_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)
