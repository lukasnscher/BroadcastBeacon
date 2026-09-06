# test_broadcastbeacon.py
"""
Tests for BroadcastBeacon module.
"""

import unittest
from broadcastbeacon import BroadcastBeacon

class TestBroadcastBeacon(unittest.TestCase):
    """Test cases for BroadcastBeacon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BroadcastBeacon()
        self.assertIsInstance(instance, BroadcastBeacon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BroadcastBeacon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
