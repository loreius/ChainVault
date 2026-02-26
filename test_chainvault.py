# test_chainvault.py
"""
Tests for ChainVault module.
"""

import unittest
from chainvault import ChainVault

class TestChainVault(unittest.TestCase):
    """Test cases for ChainVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainVault()
        self.assertIsInstance(instance, ChainVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
