# test_yarnveil.py
"""
Tests for YarnVeil module.
"""

import unittest
from yarnveil import YarnVeil

class TestYarnVeil(unittest.TestCase):
    """Test cases for YarnVeil class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = YarnVeil()
        self.assertIsInstance(instance, YarnVeil)
        
    def test_run_method(self):
        """Test the run method."""
        instance = YarnVeil()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
