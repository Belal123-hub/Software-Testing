import unittest

from main import Solution


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        """
        Test the example case from the problem statement.
        """
        self.assertEqual(self.solution.uniquePaths(3, 7), 28)

    def test_minimum_grid(self):
        """
        Test the smallest possible grid (1x1).
        """
        self.assertEqual(self.solution.uniquePaths(1, 1), 1)

    def test_single_row_grid(self):
        """
        Test a grid that has only one row (1xm).
        """
        self.assertEqual(self.solution.uniquePaths(1, 5), 1)

    def test_single_column_grid(self):
        """
        Test a grid that has only one column (nx1).
        """
        self.assertEqual(self.solution.uniquePaths(5, 1), 1)

    def test_large_grid(self):
        """
        Test a larger grid to check for performance issues and correct calculation.
        """
        self.assertEqual(self.solution.uniquePaths(100, 100), 22750883079422934966181954039568885395604168260154104734000)

    def test_medium_grid(self):
        """
        Test a grid with moderate size.
        """
        self.assertEqual(self.solution.uniquePaths(10, 10), 48620)

    def test_asymmetric_grid(self):
        """
        Test a non-square grid.
        """
        self.assertEqual(self.solution.uniquePaths(5, 10), 715)

if __name__ == '__main__':
    unittest.main()
