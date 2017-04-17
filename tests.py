import os
import unittest

from config import basedir
from app import app, db
from app.models import Cunt, Reason

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, 'test.db')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_reason(self):
        r = Reason(detail="He's a cunt")
        c1 = Cunt(name="John Terry", dickhead=r)
        c2 = Cunt(name="Ashley Cole", dickhead=r)
        db.session.add(r)
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()
        print(r.detail)
        print(c1.name, r.detail)
        print(c2.name, r.id)
