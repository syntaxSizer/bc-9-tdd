import unittest
from super_sum import super_sum

class TestSuperSum(unittest.TestCase):

    # def setUp(self):  


    def test_sum_one(self):
        ''' Test sum of elements in given one list and should return 30'''
        self.assertEqual(super_sum(10,5,6,9), 30)

    def test_sum_two(self):
        ''' Test sum of elements in a given list and number should return the total sum '''
        self.assertEqual(super_sum([10,5], 5, 20), 40)

    def test_sum_three(self):
        ''' Test sum of elements in a given list and number should return the total sum which is 30 '''
        self.assertEqual(super_sum([5,6], [4,5], 10), 30)

    def test_sum_four(self):
        ''' test sum of elements in given lists and add to integer'''
        self.assertEqual(super_sum([5,6], [4,5], [1,2]), 23)

    def test_five(self):
        '''assert throwing of exceptions if  a string  is passed'''
        result = super_sum('')
        self.assertNotEqual(type(result), int , 'The input should be an integer')

    def test_six(self):
        '''assert throwing of exceptions if  a string  is passed'''
        self.assertNotEqual(super_sum(''), None , msg= 'should return /None')

    def test_seven(self):
        '''assert whether the total is in a list'''
        self.assertIn(super_sum(1,2,3), [6,8,9,10] , msg= 'The result is not in a list')

if __name__ == '__main__':
    unittest.main()
