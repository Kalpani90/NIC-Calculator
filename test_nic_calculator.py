import unittest
import nic_calculator


class TestNicCalculator (unittest.TestCase):

    def test_get_born_date_for_male(self):
        nic = "197900209871"
        born_date = nic_calculator.get_born_date(nic)
        born_year = born_date.year
        born_month = born_date.month
        born_day = born_date.day

        self.assertEqual(born_year,1979)
        self.assertEqual(born_month,1)
        self.assertEqual(born_day,2)

    def test_get_born_date_for_female(self):
        nic = "197950209871"
        born_date = nic_calculator.get_born_date(nic)
        born_year = born_date.year
        born_month = born_date.month
        born_day = born_date.day

        self.assertEqual(born_year,1979)
        self.assertEqual(born_month,1)
        self.assertEqual(born_day,2)

    def test_validate_nic(self):
        nic = "197950209871"
        length = nic_calculator.validate(nic)
        expect_result = True
      
        self.assertEqual(length,expect_result)

    def test_validate_nic_digit(self):
        nic = "197950209871"

        self.assertTrue(nic.isdigit())

    def test_get_born_year(self):
        nic = "197950209871"
        born_year = nic_calculator.get_born_year(nic)

        self.assertEqual(born_year,1979)


if __name__ == '__main__':
    unittest.main()



