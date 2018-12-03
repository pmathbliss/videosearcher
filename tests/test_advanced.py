# -*- coding: utf-8 -*-

from .context import videosearcher

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(videosearcher.hmm())


if __name__ == '__main__':
    unittest.main()

