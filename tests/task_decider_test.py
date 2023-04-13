import unittest
from src.task_decider import *
from src.tasks import *


class TestTask_Decider(unittest.TestCase):

    def setUp(self):
        self.wash_dish_task = Task("wash dishes", "15 minutes")
        self.cook_dinner = Task("cook dinner", "1 hour")
        self.clean_windows = Task("clean windows", "1 hour 15 minutes")

    def test_dishes_and_cooking(self):
        self.assertEqual("wash dishes", task_decider(self.wash_dish_task, self.cook_dinner))

    def test_cooking_and_windows(self):
        self.assertEqual("cook dinner", task_decider(self.cook_dinner, self.clean_windows))

    def test_windows_and_dishes(self):
        self.assertEqual("clean windows", task_decider(self.clean_windows, self.wash_dish_task)) 

    
# this is coming back as None -> task_decider(self.first_task, self.second_task
