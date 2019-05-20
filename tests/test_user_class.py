import unittest
from model.user import User


class UserTestCase(unittest.TestCase):

    def test_password_setter(self):
        u = User()
        u.password = 'kitten'
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='kitten')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='kitten')
        self.assertTrue(u.verify_password('kitten'))
        self.assertFalse(u.verify_password('Kittens'))

    def test_passwords_hashes_are_random(self):
        u1 = User(password='kitten')
        u2 = User(password='kitten')
        self.assertTrue(u1.password_hash != u2.password_hash)

