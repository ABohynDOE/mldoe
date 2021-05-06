import unittest
from src.mldoe.design import TLD, MLD


class TestWLPValues(unittest.TestCase):
    """
    Test the WLP property of two-level design class (TLD) using the WLP presented in Chen, Sun and Wu (1993) as a
    reference.
    For each value of N (number or runs) in {16,32}, two designs have been randomly selected from the catalog and
    their computed WLP is evaluated against the one presented in the catalog.
    """

    def test_TLD_CSW_N16(self):
        cols_lst = [[1, 2, 4, 8, 3, 5, 6, 9, 10, 13],
                    [1, 2, 4, 8, 3, 5, 6, 9, 10, 12]]
        wlp_lst = [(9.0, 16.0, 15.0, 12.0, 7.0, 3.0, 1.0, 0.0),
                   (10.0, 15.0, 12.0, 15.0, 10.0, 0.0, 0.0, 1.0)]
        for idx, cols in enumerate(cols_lst):
            des = TLD(16, cols)
            self.assertTrue(des.wlp[3:] == wlp_lst[idx])

    def test_TLD_CSW_n32(self):
        cols_lst = [[1, 2, 4, 8, 16, 3, 5, 14, 22, 26, 29],
                    [1, 2, 4, 8, 16, 3, 13, 21]]
        wlp_lst = [(2.0, 16.0, 16.0, 12.0, 10.0),
                   (1.0, 3.0, 2.0, 0.0, 1.0)]

        for idx, cols in enumerate(cols_lst):
            des = TLD(32, cols)
            self.assertTrue(des.wlp[3:8] == wlp_lst[idx])


if __name__ == "__main__":
    unittest.main(verbosity=2)
