import datetime
import unittest
from unittest.mock import patch

from main import define_focus_factor, calculate_working_days, calculate_project_end_date


class TestProjectPlan(unittest.TestCase):

    def test_define_focus_factor(self):
        self.assertEqual(define_focus_factor(150), 1)
        self.assertEqual(define_focus_factor(50), 0.5)
        self.assertEqual(define_focus_factor(0.5), 0.5)

    @patch("main.holidays.MX")
    def test_calculate_working_days(self, mock_holidays):
        mock_holidays.return_value = {
            datetime.date(2023, 1, 1),
            datetime.date(2023, 1, 2),
        }
        start_date = datetime.datetime(2023, 1, 1)
        total_hours = 16
        end_date, working_days = calculate_working_days(
            start_date, total_hours, mock_holidays()
        )
        self.assertEqual(working_days, 2)
        self.assertEqual(end_date, datetime.datetime(2023, 1, 4))

    @patch("main.holidays.MX")
    def test_calculate_project_end_date(self, mock_holidays):
        mock_holidays.return_value = {datetime.date(2023, 1, 1)}
        start_date = datetime.datetime(2023, 1, 1)
        tasks = [("Task 1", 8), ("Task 2", 8)]  # 2 days of work
        total_points, task_end_dates = calculate_project_end_date(
            start_date, 1, [1], 1, 0, 0, tasks
        )
        self.assertEqual(total_points, 16)
        self.assertEqual(len(task_end_dates), 2)
        self.assertTrue(all(isinstance(date, datetime.date) for date in task_end_dates))


if __name__ == "__main__":
    unittest.main()
