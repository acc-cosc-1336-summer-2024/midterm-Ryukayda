import unittest

# Importing the functions to test from their respective modules
from src.question_a.question_a import test_config as test_config_a, use_global, global_var as global_var_a
from src.question_b.question_b import get_miles_per_hour
from src.question_c.question_c import is_prime
from src.question_d.question_d import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config_a())

    def test_use_global(self):
        from src.question_a import question_a
        # Reset the global variable for the test
        question_a.global_var = 0
        # Call the function that modifies the global variable
        question_a.use_global()
        # Assert that the global variable has changed
        self.assertEqual(question_a.global_var, 1, f"Expected global_var to be 1, but got {question_a.global_var}")

class TestGetMilesPerHour(unittest.TestCase):

    def test_get_miles_per_hour(self):
        kilometers = 32
        minutes = 60
        expected_result = 19.883872
        result = get_miles_per_hour(kilometers, minutes)
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_get_miles_per_hour_invalid_arguments(self):
        result = get_miles_per_hour(-1, 60)
        self.assertEqual(result, 'Invalid arguments')
        result = get_miles_per_hour(32, -1)
        self.assertEqual(result, 'Invalid arguments')

class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(11))

class TestGetDayOfWeek(unittest.TestCase):

    def test_get_day_of_week(self):
        self.assertEqual(get_day_of_week(0), "Invalid number")
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")
        self.assertEqual(get_day_of_week(8), "Invalid number")

if __name__ == '__main__':
    unittest.main()
