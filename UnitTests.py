import unittest
from parameterized import parameterized

from main import Solution


class TestUniquePaths(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Setup that runs once before any test in the class.
        """
        cls.solution = Solution()

    @classmethod
    def tearDownClass(cls):
        """
        Teardown that runs once after all tests in the class.
        """
        pass

    def setUp(self):
        """
        Setup that runs before each test.
        """
        self.solution = Solution()

    def tearDown(self):
        """
        Teardown that runs after each test.
        """
        pass

    @parameterized.expand([
        ("example_case", 3, 7, 28),
        ("minimum_grid", 1, 1, 1),
        ("single_row_grid", 1, 5, 1),
        ("single_column_grid", 5, 1, 1),
        ("medium_grid", 10, 10, 48620),
        ("asymmetric_grid", 5, 10, 715),
    ])
    def test_unique_paths(self, name, m, n, expected):
        """
        Parameterized test for various grid sizes.
        """
        self.assertEqual(self.solution.uniquePaths(m, n), expected)

    def test_large_grid(self):
        """
        Test a larger grid to check for performance issues and correct calculation.
        """
        self.assertEqual(self.solution.uniquePaths(100, 100),
                         22750883079422934966181954039568885395604168260154104734000)

    def test_invalid_input(self):
        """
        Test that invalid inputs raise an exception.
        """
        with self.assertRaises(ValueError):
            self.solution.uniquePaths(0, 100)
        with self.assertRaises(ValueError):
            self.solution.uniquePaths(100, 0)
        with self.assertRaises(ValueError):
            self.solution.uniquePaths(101, 100)
        with self.assertRaises(ValueError):
            self.solution.uniquePaths(100, 101)

    # Stub to simulate external interaction (if needed)
    def test_stub_example(self):
        """
        Example of a test stub. Here we simulate an environment for the test.
        """
        # Assuming there's a complex method we want to stub out
        # As the current code doesn't have such a method, this is illustrative
        original_method = self.solution.uniquePaths
        self.solution.uniquePaths = lambda m, n: 42  # Mocking the method

        try:
            self.assertEqual(self.solution.uniquePaths(10, 10), 42)
        finally:
            self.solution.uniquePaths = original_method


if __name__ == '__main__':
    unittest.main()
