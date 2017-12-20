from unittest import TestCase
from chronos.services.Event import Event
from test.test_utils.Listener import Listener

class TestEvent(TestCase):
    def test_subscribe(self):
        # Create event
        e = Event()
        self.assertTrue(e.empty())

        # Instantiate test objects
        L1 = Listener()
        L2 = Listener()

        # Subscribe function to event
        success = e.subscribe(L1.foo)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 1)

        # Subscribe the same function to event
        success = e.subscribe(L1.foo)
        self.assertFalse(success)
        self.assertEqual(e.getSubCount(), 1)

        # Subscribe function to event
        success = e.subscribe(L1.foo2)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 2)

        # Subscribe 2 function to event
        success = e.subscribe(L2.foo)
        self.assertTrue(success)
        success = e.subscribe(L2.foo2)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 4)

    def test_unsubscribe(self):
        # Create event
        e = Event()
        self.assertTrue(e.empty())

        # Instantiate test objects
        L1 = Listener()
        L2 = Listener()

        # Subscribe 4 function to event
        success = e.subscribe(L1.foo)
        self.assertTrue(success)
        success = e.subscribe(L1.foo2)
        self.assertTrue(success)
        success = e.subscribe(L2.foo)
        self.assertTrue(success)
        success = e.subscribe(L2.foo2)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 4)

        # Unsubscribe 1 function
        success = e.unsubscribe(L1.foo)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 3)

        # Unsubscribe the same function
        success = e.unsubscribe(L1.foo)
        self.assertFalse(success)
        self.assertEqual(e.getSubCount(), 3)

    def test_fire(self):
        # Create event
        e = Event()
        self.assertTrue(e.empty())

        # Instantiate test objects
        L1 = Listener()
        L2 = Listener()

        # Subscribe 2 functions
        success = e.subscribe(L1.set_message)
        self.assertTrue(success)
        success = e.subscribe(L2.set_message)
        self.assertTrue(success)

        # Fire event on 2 listeners
        msg1 = "TEST"
        e.fire(msg=msg1)
        self.assertEqual(L1.s, msg1)
        self.assertEqual(L2.s, msg1)

        # Unsub 1 listener
        e.unsubscribe(L2.set_message)

        # Fire event on the remaining listener
        msg2 = "WOW"
        e.fire(msg=msg2)
        self.assertEqual(L1.s, msg2)
        self.assertEqual(L2.s, msg1)

    def test_getSubCount(self):
        # Create event
        e = Event()
        self.assertTrue(e.empty())
        self.assertEqual(e.getSubCount(), 0)

        # A local class for testing
        L1 = Listener()
        L2 = Listener()

        # Subscribe a number of listener handlers, monitoring the count
        success = e.subscribe(L1.foo)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 1)

        success = e.subscribe(L1.foo2)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 2)

        success = e.subscribe(L2.foo)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 3)

        success = e.subscribe(L2.foo2)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 4)

        # Unsubscribe until they are all gone
        success = e.unsubscribe(L1.foo)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 3)

        success = e.unsubscribe(L1.foo2)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 2)

        success = e.unsubscribe(L2.foo)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 1)

        success = e.unsubscribe(L2.foo2)
        self.assertTrue(success)
        self.assertEqual(e.getSubCount(), 0)

    def test_empty(self):
        # Create event
        e = Event()
        self.assertTrue(e.empty())

        # A local class for testing
        L1 = Listener()

        # Subscribe a number of listener handlers, monitoring the count
        e.subscribe(L1.foo)
        self.assertFalse(e.empty())
