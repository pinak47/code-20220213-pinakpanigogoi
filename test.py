import unittest
from src import fitness_calc as fitness
import utility

# unittest will test all the methods whose name starts with 'test', standard python library

class SampleTest(unittest.TestCase):

    def test_bmi(self):
        ft_cal = fitness.fitness_calculation()
        df_test = utility.utility_main().read_json("test_data.json")
        df_cal = ft_cal.BMI_calc("person_detail.json")
        self.assertEqual(True, df_test.equals(df_cal))
       

# running the test
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
 