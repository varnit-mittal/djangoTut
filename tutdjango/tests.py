from django.test import TestCase
from django.conf import Settings
from django.contrib.auth.password_validation import validate_password
import os

class TryDjangoConfigTest(TestCase):
    def test_seckretKeyStrength(self):
        SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY')
        # SECRET_KEY=Settings.SECRET_KEY
        # self.assertNotEqual(SECRET_KEY,)
        try:
            is_strong=validate_password(SECRET_KEY)
        except Exception as e:
            msg=f'Weak Secret Key {e.messages}'
            self.fail(msg)