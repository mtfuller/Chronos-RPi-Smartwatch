from unittest import TestCase
from chronos.services.Service import Service
from test.test_utils.Listener import Listener

class TestService(TestCase):
    def test_add_event(self):
        # Setup
        s = Service()
        L1 = Listener()

        # Make sure that listener hasn't been touched
        self.assertTrue(L1.equals(""))

        # Add first event
        e1 = "EVENT1"
        e2 = "EVENT2"
        success = s.add_event(e1)
        self.assertTrue(success)

        # Add second event
        success = s.add_event(e2)
        self.assertTrue(success)

        # Try to erroneously add event again
        success = s.add_event(e2)
        self.assertFalse(success)

        # Subscribe listener to Event 1 and fire the event
        msg0 = "WOWZA"
        s.get_event(e1).subscribe(L1.set_message)
        s.get_event(e1).fire(msg=msg0)
        self.assertTrue(L1.equals(msg0))

        # Subscribe listener to Event 2 and test firing both events
        s.get_event(e2).subscribe(L1.set_message)

        msg1 = "NUM1"
        s.get_event(e1).fire(msg=msg1)
        self.assertTrue(L1.equals(msg1))

        msg2 = "NUM2"
        s.get_event(e2).fire(msg=msg2)
        self.assertTrue(L1.equals(msg2))

    def test_get_event(self):
        # Setup
        s = Service()
        e = "EVENT1"
        s.add_event(e)

        # Make sure that it returns either an instance of an Event or None
        self.assertEqual(type(s.get_event(e)).__name__,"Event")
        self.assertEqual(s.get_event("NO_EVENT"), None)

    def test_has_event(self):
        # Setup
        s = Service()
        e = "EVENT1"
        s.add_event(e)

        self.assertTrue(s.has_event(e))
        self.assertFalse(s.has_event("NO_EVENT"))

    def test_get_event_count(self):
        # Setup
        s = Service()

        # Check with no events
        self.assertEqual(s.get_event_count(), 0)

        # Add events and check count
        s.add_event("EVENT1")
        self.assertEqual(s.get_event_count(), 1)

        s.add_event("EVENT2")
        self.assertEqual(s.get_event_count(), 2)

        s.add_event("EVENT3")
        self.assertEqual(s.get_event_count(), 3)

    def test_empty(self):
        # Setup
        s = Service()

        # Check with no events
        self.assertTrue(s.empty())

        # Add events and check empty
        s.add_event("EVENT1")
        self.assertFalse(s.empty())
