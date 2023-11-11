import unittest
from math_quiz import number_picker, operator, calculate


class TestMathGame(unittest.TestCase):

    def test_number_picker(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = number_picker(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operator(self):
        # TEST 2 check if operators chosen in the function operator() are correct
        allowed_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operand = operator()
            self.assertIn(operand, allowed_operators)
        pass

    def test_calculate(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 3, '+', '6 + 3', 9),
                (8, 5, '*', '8 * 5', 40),
                (9, 5, '-', '9 - 5', 4),
                (10, 8, '*', '10 * 8', 80),
                (7, 6, '+', '7 + 6', 13),
                (10, 3, '-', '10 - 3', 7),
                (4, 6, '*', '4 * 6', 24),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # Test 3
                problem, answer = calculate(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
