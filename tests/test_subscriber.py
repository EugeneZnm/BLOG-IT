import unittest

from app.models import User


class SubscriberModelTest(unittest.TestCase):
    def setUp(self):
        self.new_subscriber = Subscriber(username = 'eugene', email = 'eugenenzioki@gmail.com')

    # subscriber saving
    def save_subscriber(self):
        db.session.add(self.new_subscriber)
        db.session.commit()
