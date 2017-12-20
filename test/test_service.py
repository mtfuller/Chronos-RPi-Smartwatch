from unittest import TestCase
from chronos.services.Service import Service
from test.test_utils.Listener import Listener

class TestService(TestCase):
    def test_add_event(self):
        s = Service()

        L1 = Listener()

        self.assertTrue(L1.equals(""))

        success = s.add_event("EVENT1")
        self.assertTrue(success)

        success = s.add_event("EVENT2")
        self.assertTrue(success)

        success = s.add_event("EVENT2")
        self.assertFalse(success)

        msg0 = "WOWZA"
        s.get_event("EVENT1").subscribe(L1.set_message)
        s.get_event("EVENT1").fire(msg=msg0)
        self.assertTrue(L1.equals(msg0))

        s.get_event("EVENT2").subscribe(L1.set_message)

        msg1 = "NUM1"
        s.get_event("EVENT1").fire(msg=msg1)
        self.assertTrue(L1.equals(msg1))

        msg2 = "NUM2"
        s.get_event("EVENT2").fire(msg=msg2)
        self.assertTrue(L1.equals(msg2))

    def test_get_event(self):
        s = Service()

        s.add_event("EVENT1")

        self.assertEqual(type(s.get_event("EVENT1")).__name__,"Event")
        self.assertEqual(s.get_event("NO_EVENT"), None)

    def test_has_event(self):
        s = Service()

        e = "EVENT1"
        s.add_event(e)

        self.assertTrue(s.has_event(e))
        self.assertFalse(s.has_event("NO_EVENT"))

    def test_get_event_count(self):
        s = Service()

        self.assertEqual(s.get_event_count(), 0)
        s.add_event("EVENT1")

        self.assertEqual(s.get_event_count(), 1)
        s.add_event("EVENT2")

        self.assertEqual(s.get_event_count(), 2)
        s.add_event("EVENT3")

        self.assertEqual(s.get_event_count(), 3)
