from yt.yt_analysis.statistics import stats
import unittest


class test_stats(unittest.TestCase):


    def __init__(self):
        pass

    def setUp(self):
        pass

    def print_stats(self):
        x = stats.print_stats()
        self.assertEqual(len(x), 4)

    def tearDown(self):
        pass









