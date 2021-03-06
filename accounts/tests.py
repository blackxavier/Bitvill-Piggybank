from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTests(TestCase):
    """[This testcase is used to test user and superuser creation]

    Args:
        TestCase ([User object]): [Creates a user and uses the return object for testing ]
    """

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser("testuser@super.com", "password")
        self.assertEqual(super_user.email, "testuser@super.com")

        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "User - testuser@super.com")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="testuser@super.com",
                password="password",
                is_superuser=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="testuser@super.com",
                password="password",
                is_staff=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="",
                username="username1",
                first_name="first_name",
                password="password",
                is_superuser=True,
            )

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user("testuser@user.com", "password")
        self.assertEqual(user.email, "testuser@user.com")

        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(email="", password="password")
