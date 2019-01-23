import unittest
from deter_lib import deter2x2

class TestDeter(unittest.TestCase):
    """
    """
    def do_test(self,a,b,c,d):
        matrix_2x2 = [[a,b],[c,d]]
        expected_result = a*d - b*c
        actual_result = deter2x2(matrix_2x2)
        self.assertEqual(expected_result, actual_result)


    def test_determinant(self):
        """
        """
        self.do_test(3,1,4,5)

    def test_determinant2(self):
        """
        """
        self.do_test(2,7,-4,-5)

    def test_determinant3(self):
        """
        """
        self.do_test(-3,0,-4,-5)


if __name__=='__main__':
    unittest.main()
